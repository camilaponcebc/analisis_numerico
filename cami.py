# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
dir(math)
#EJERCICIO 1 DE CLASE

F = float(input('ingrese un valor para la temperatura en grados Farenheit: '))

C = (F-32)*5/9

print(f'Temperatura en grados celsuis es {C}')

#EJERCICIO 2 DE CLASE
x=5
a=math.sinh(5)
print('El seno hiperbolico de 5 es', a)

b=(math.e**x-math.e**-x)/2
print('La ecuación a es igual a: ', b)

c = ((math.exp(x)-math.exp(-x))/2)
print('La ecuación a es igual b: ', c)

z1=8+4j
z2=2j
w=z1+z2
w.conjugate()
#w.imag
#w.real


