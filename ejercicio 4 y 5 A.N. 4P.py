# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
#Ejercicio 4.

va=complex((input('ingresa el valor de a: ')))
vb=complex((input('ingresa el valor de b: ')))
vc=complex((input('ingresa el valor de c: ')))

print('Para resolver')

disc = (vb)**2-(4*va*vc)


z1 = (-vb+np.sqrt(disc))/(2*va)
z2 = (-vb-np.sqrt(disc))/(2*va)
print(f'Las raíces son: {z1} y {z2}')

#Ejercicio 5.
from sympy import (symbols, tan, cos, rad)
#¿Cuál es la trayectoria de una pelota que se lanza con una rapidéz inicial Vo
#a un ángulo (theta) medido de la horizontal?

#simbolos
x, v0, theta, g, y0 = symbols('x v0 theta g y0')

x=float(input('ingrese el valor de x (en metros): ')) #distancia recorrida
v0 = float(input('ingrese el valor de v0 (m/s): ')) #velocidad inicial
theta = float(input('ingrese el valor de theta (en grados): '))
g= 9.81 #(m/s**2)
y0 =float(input('ingrese el valor de y0 (en metros): ')) #altura inicial

theta = rad(theta)

#Ecuación de la trayectoria
f_x = x * tan(theta) - (g /(2*v0**2))*(x**2/cos(theta)**2)+y0

print("Ecuación de la trayectoria simbólica:")
print(f_x)

    
