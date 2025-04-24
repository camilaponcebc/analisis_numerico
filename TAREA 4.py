# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 20:05:25 2025

@author: camil
"""
import math

"""
10. Escribe un programa que calcule todas las raíces de f(x)=0 en un intervalo
dado utilizando el método de Ridder. Usa las funciones rootsearch y ridder.
Puedes usar el programa del Ejemplo 4.3 como modelo.
11. Prueba el programa encontrando las raíces de f(x)=xsin(x)+3cos(x)−x en el
intervalo (−6,6).
"""

def f(x): return x * math.sin(x) + 3 * math.cos(x) - x
def df(x): return x * math.cos(x) - 2 * math.sin(x) - 1
#math.sin(x) + x * math.cos(x) - 3 * math.sin(x) - 1


# Metodo de Biseccion
x1 = -6                # primer valor del intervalo
x2 = 6               # segudo valor del intervalo
y1 = f(x1)    # calcula y1
y2 = f(x2)   # calcula y2
if y1*y2 > 0:          # prueba si los signos son iguales
    print('No hay raices en el intervalo dado')
    exit              # termina el programa  #falta encontrar el buen EXIT!!
for i in range(1,101): # asume que 100 bisecciones son suficientes
  xh = (x1+x2)/2         # calcula el valor medio
  yh =  f(xh)    # calcula el valor de y en el valor medio yh
  if abs(yh) < 1.0e-6:   # condicion de acercamiento a la solucion (tol)
    break                  # salir del loop
  elif y1*yh < 0:        # si el signo es diferente quedarse en la primera mitad
    x2 = xh                # que x2 sea el punto medio
  else:                  # si el signo es igual quedarse en la segunda mitad
    x1 = xh                # que x1 sea el punto medio
print('La raiz es: %.5f' % x1)
print('Numero de bisecciones: %d' % i)

def newtonRaphson(x,tol=1.0e-9):
  for i in range(30):
    dx = -f(x)/df(x)
    x = x + dx
    if abs(dx) < tol: return x,i
  print('Too many iterations\n')

root,numIter = newtonRaphson(-6)
print('Root =',root)
print('Number of iterations =',numIter)


"""
La velocidad v de un cohete Saturno V en vuelo vertical cerca de la superficie
de la Tierra puede aproximarse por la fórmula v = u * ln(M0/(M0-mt) - g*t)
Determina el tiempo en que el cohete alcanza la velocidad del sonido (335 m/s).
"""
#v = u * ln(M0/(M0-mt) - g*t)
 
u = 2510 # m/s 
M0 = 2.8e6 # kg 
m = 13.3e3 # kg/s 
g = 9.81 # m/s^2
v = 335 # m/s 

def f(t): return u * math.log(M0 / (M0 - m * t)) - g * t - v
def df(t): return (u * m) / (M0 - m * t) - g
 
def newtonRaphson(t,tol=1.0e-9):
  for i in range(30):
    dt = -f(t)/df(t)
    t = t + dt
    if abs(dt) < tol: return t,i
  print('Too many iterations\n')

root,numIter = newtonRaphson(10)
print('Root =',root)
print('Number of iterations =',numIter)


"""
9. Use the data in the table to compute f'(0.2) as accurately: as possible:
x | 0 | 0.1 | 0.2 | 0.3 | 0.4 |
f(x) | 0.000000 | 0.078348 | 0.138910 | 0.192916 | 0.244981 |
"""
xd = [0, 0.1, 0.2, 0.3, 0.4]
fd = [0.000000, 0.078348, 0.138910, 0.192916, 0.244981]

# Diccionario de valores para facilitar la consulta
def f(x, n):
    vals = {
        0.0: 0.000000,
        0.1: 0.078348,
        0.2: 0.138910,
        0.3: 0.192916,
        0.4: 0.244981}
    
    return round(vals[round(x, 1)], n)

# Derivada central
def d1fc(x, h, f, n):
    return (f(x + h, n) - f(x - h, n)) / (2 * h)

h = 0.1
x = 0.2
n = 6  
central = d1fc(x, h, f, n)
print(f"Derivada central: {central}")

"""
10. Using five significant figures in the computations, determine d(sin x)/dx at x =
0.8 from (a) the first forward difference approximation and (b) the first central
difference approximation. In each case, use h that gives the most accurate result
(this requires experimentation).
"""
from math import sin, cos

def dff(f,x,h): #Segunda derivada de f con aproximación forward con n decimales
  dff=(f(x + h) - f(x)) / h
  return dff

def dfc(f,x,h): #Segunda derivada de f con aproximación central con n decimales
  dfc = (f(x + h) - f(x - h)) / (2*h)
  return dfc

exact = round(cos(0.8), 10)

x = 0.8
h_val = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]

print("Usando 5 cifras significativas:")
print("\n(a) Forward difference:")
for h in h_val:
    approx = round(dff(sin, x, h), 5)
    error = abs((approx - exact) / exact) * 100
    print(f"h = {h:.0e} | Aproximación = {approx:.5f} | Error relativo = {error:.5f}%")

print("\n(b) Central difference:")
for h in h_val:
    approx = round(dfc(sin, x, h), 5)
    error = abs((approx - exact) / exact) * 100
    print(f"h = {h:.0e} | Aproximación = {approx:.5f} | Error relativo = {error:.5f}%")
"""
6.1
1.  Use the recursive trapezoidal rule to evaluate 3 π/4|0 ln(1 + tan x)dx.
Explain the results.
"""

def f(x):
    return math.log(1 + math.tan(x))

def trapecio_recursiva(f, a, b, Iold, k):
    if k == 1:
        Inew = (f(a) + f(b)) * (b - a) / 2.0
    else:
        n = 2 ** (k - 2) 
        h = (b - a) / n  
        x = a + h / 2.0
        sum = 0.0
        for i in range(n):
            sum = sum + f(x)
            x = x + h
        Inew = (Iold + h * sum) / 2.0
    return Inew

a = 0
b = 3 * math.pi / 4
Iold = (f(a) + f(b)) * (b - a) / 2.0  
k = 2  

result = trapecio_recursiva(f, a, b, Iold, k)
print(f'Valor aproximado de la integral: {result}')
