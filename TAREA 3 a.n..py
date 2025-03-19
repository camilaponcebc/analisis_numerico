# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 20:07:04 2025

@author: camil
"""
#TAREA 3
#Camila Ponce Becerra

import numpy as np
import matplotlib.pyplot as plt
from math import *

# 1. La viscocidad cinética del agua varía con la temperatura de la siguiente manera:
#  T(°C) | uk(10**-3 m**2/s)
#  0	     0.101
#  21.1	 1.79
#  37.8	 1.13
#  54.4	 0.696
#  71.1	 0.519
#  87.8	 0.338
#  100	 0.296

# Utilice el método de su preferencia para interpolar uk en T = 10°, 30°, 60° y 90°C.

# Función para evaluar el polinomio de Newton
def evalPoly(a, xData, x):  # Función que evalua polinomios de Lagrange
    n = len(xData) - 1  # Grado del polinomio
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - xData[n - k]) * p
    return p

xData = np.array([0, 21.1, 27.8,54.4,71.1,87.8,100])
yData = np.array([0.101,1.79,1.13,0.696,0.519,0.338,0.296])

def coeffts(xData, yData):
    m = len(xData)  # Número de datos
    a = yData.copy() # Copiar los valores de yData
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k - 1]) / (xData[k:m] - xData[k - 1])
    return a

coeff = coeffts(xData, yData)

# Temperaturas en las que queremos interpolar
x_vals = np.array([10, 30, 60, 90])

# Grafica de datos originales y del polinomio interpolado
x_plot = np.linspace(0, 100, 500)
y_plot = [evalPoly(coeff, xData, xi) for xi in x_plot]

plt.plot(x_plot, y_plot, "r", label="Interpolación de Newton")
plt.plot(xData, yData, "bo", label="Datos originales")
plt.legend()
plt.grid()
plt.title("Interpolación de Newton")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Viscosidad cinética (10^-3 m^2/s)")
plt.show()

print("  x     yInterpolado")
print("------------------------")
for x in x_vals:
    yInterpolado = evalPoly(coeff, xData, x)
    print(f" {x:.1f}   {yInterpolado:.8f}")


# 2. La tabla muestra como la densidad relativa p del aire varía con la altura h.
#Determine mediante interpolación de Lagrange la densidad relativa del aire a 10.5 km.
# h(km) |   p
#   0	|   1
# 1.525	| 0.8617
# 3.050	| 0.7385
# 4.575	| 0.6292
# 6.10	| 0.5328
# 7.625	| 0.4481
# 9.150	| 0.3741

from scipy.interpolate import lagrange

x= np.array([0, 1.525, 3.050, 4.575, 6.10, 7.625, 9.150])  # altura (h)
y = np.array([1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])  # densidad relativa (p)

#polinomio de Lagrange usando los puntos dados
L = lagrange(x, y)

xp = 10.5  # altura en km
yp = L(xp) 

print(f"Para h = {xp} km, la densidad relativa es: {yp:.4f}")


x_vals = np.linspace(min(x), max(x), 100)  
y_vals = L(x_vals) 

plt.plot(x_vals, y_vals, label="Interpolación de Lagrange", linestyle="--")
plt.scatter(x, y, color="red", label="Datos Originales")
plt.scatter(xp, yp, color="blue", zorder=5)
plt.text(xp, yp, f"({xp}, {yp:.4f})", fontsize=12, verticalalignment="bottom")

plt.xlabel("Altura (km)")
plt.ylabel("Densidad Relativa (p)")
plt.title("Interpolación de Lagrange")
plt.legend()
plt.grid(True)
plt.show()


# 3. La amplitud vibracional de un eje de transmisión es medida a varias velocidades.
# Los resultados son:
#velocidad(rpm) | amplitud(mm)
#       0             0
#      400	         0.072
#      800	         0.233
#      1200	        0.712
#      1600	         3.400
# Utilice el método de interpolación más conveniente para graficar amplitud vs velocidad
# de 0 a 2500rpm (observe los intervalos de la tabla y determine el tamaño más conveniente
#                 de los intervalos).

velocidad = [0, 400, 800, 1200, 1600]
amplitud = [0, 0.072, 0.233, 0.712, 3.400]

#polinomio de Lagrange
polinomio = lagrange(velocidad, amplitud)

#rango de velocidades de 0 a 2500 rpm 
velocidad_interpolada = np.linspace(0, 2500, 100)

# valores de amplitud correspondientes a cada velocidad
amplitud_interpolada = polinomio(velocidad_interpolada)

plt.plot(velocidad_interpolada, amplitud_interpolada, label="Interpolación de Lagrange")
plt.scatter(velocidad, amplitud, color='red', zorder=5, label="Datos Originales")

plt.xlabel("Velocidad (rpm)")
plt.ylabel("Amplitud (mm)")
plt.title("Interpolación de Amplitud vs Velocidad")
plt.legend()
plt.grid(True)

plt.show()
