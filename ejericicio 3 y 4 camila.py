# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:56:07 2025

@author: CC_20
"""

#Numeros complejos
#EJERCICIO 3
import math
from cmath import sin, sinh, cos, e, exp
#1° ejercicio:
x = complex(input('Ingrese un numero: \n'))
print('sin(i',x, ')=', sin(x*1j))
print('isinh(',x, ')=', 1j*sinh(x))

#2° ejercicio. Considera la relación de Euler para x real
i = complex(input('Ingrese un numero: \n'))
sm = cos(x) + i*sin(x)
xp =exp(i*x)
eu = e(xp)
print('e^i*x=', 'cos(',x,') + isin(',x,')')
print(eu,'=', sm)

