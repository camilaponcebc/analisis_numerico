# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 10:45:47 2025

@author: camil
"""
import numpy as np
# Ejercicio 1. Interseccion de trayectorias.
#Tres objetos se mueven de tal manera que sus trayectorias son:
#Encontrar su punto de intersección.

#matriz de las ecuaciones:
    
a = np.array([[2, -1, 3],
              [0, 2, -1],
              [7, -5, 0]])

print('La matriz de coeficientes es:\n ', a)

b = np.array([[24], [14], [6]])
n = len(b)
print('La matriz constante es:\n ', b)

matriz_aumentada = np.concatenate((a,b), axis=1, dtype=float)
print('La matriz aumentada es :\n', matriz_aumentada)

#eliminacion de Gauss

def gaussElimin(a,b):
  # Fase de eliminacion
  for k in range(0,n-1):
    for i in range(k+1,n):
      if matriz_aumentada[i,k] != 0:
        lam = matriz_aumentada[i,k]/matriz_aumentada[k,k]
        matriz_aumentada[i] = matriz_aumentada[i] - lam*matriz_aumentada[k]
        b[i] = b[i] - lam*b[k]
        print(f'El siguiente elemento del procedimiento es:\n {matriz_aumentada}')
  # Fase de sustitucion hacia atras
  for k in range(n-1,-1,-1):
    b[k] = (b[k] - np.dot(matriz_aumentada[k,k+1:n],b[k+1:n]))/matriz_aumentada[k,k]
  return b

print('El punto de intersección es:\n',gaussElimin(a,b))

############################################################################################

#Ejercicio 2. Carga de los quarks.
"""
Los protones y neutrones están formados cada uno por tres quarks. Los protones poseen dos
quarks up (u) y un quark down (d), los neutrones poseen un quark up y dos quarks down. Si
la carga de un protón es igual al positivo de la carga del electrón +e y la carga de un
neutrón es cero, determine las cargas de los quarks up y down. (Tip: suponga que +e=1.)
 """
d = np.array([[2, 1],
              [1, 2]])
print('La matriz de coeficientes es:\n ', d)

e = np.array([[1], [0]])
n = len(e)
print('La matriz constante es:\n ', e)

matriz_aumentada = np.concatenate((d,e), axis=1, dtype=float)
print('La matriz aumentada es :\n', matriz_aumentada)

print('Las cargas de los quarks up y down son:\n', gaussElimin(d,e))

############################################################################################

#Ejercicio 3. Meteoros.
"""
El Centro de Investigación 1 examina la cantidad de meteoros que entran a la atmósfera.
Con su equipo de recopilación de datos durante 8 horas captó 95kg de meteoros, por fuentes
externas sabemos que fueron de 4 distintas masas (1kg, 5kg, 10kg y 20kg). La cantidad total
de meteoros fue de 26. Otro centro de investigación captó que la cantidad de meteoros de5kg es 4 veces la cantidad de meteoros de 10kg, y el número de meteoros de 1kg es 1 menos que el doble de la cantidad de meteoros de 5kg. Después use matrices para encontrar el número asociado a cada masa de meteoros.

"""
a1 = np.array([[1, 5, 10, 20],
              [0, 1, -4, 0],
              [-1, 2, 0, 0],
              [1, 1, 1, 1]])
print('Matriz de coeficientes:\n ', a1)

b1 = np.array([[95], [0], [1], [26]])
n = len(b1)
print('Matriz constante:\n ', b1)

matriz_aumentada = np.concatenate((a1,b1), axis=1, dtype=float)
print('Matriz aumentada:\n', matriz_aumentada)

print('La cantidad de meteoros de 1kg, 5kg, 10kg y 20kg es:\n',gaussElimin(a1,b1),"\n respectivamente")