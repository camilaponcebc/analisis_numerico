# -*- coding: utf-8 -*-
"""
Created on Wed May 21 08:22:19 2025

@author: camil
"""

#DULCE CAMILA PONCE BECERRA

import numpy as np 
import math
import matplotlib.pyplot as plt

#EJERCICIO 3 SEC. 7.1


def eulerint(F,x,y,xStop,h):
  X=[]
  Y=[]
  X.append(x)
  Y.append(y)
  while x<xStop:
    h=min(h,xStop-x)
    y=y+h*F(x,y)
    x=x+h
    X.append(x)
    Y.append(y)
  return np.array(X),np.array(Y)  

def imprimeSol(X,Y,frec):
 
  def imprimeEncabezado(n):
    print("\n x ",end=" ")
    for i in range (n):
      print(" y[",i,"] ",end=" ")
    print()

  def imprimeLinea(x, y, n):
    print("{:13.4e}".format(x), end=" ")
    if n == 1:
        print("{:13.4e}".format(y), end=" ")
    else:
        for i in range(n):
            print("{:13.4e}".format(y[i]), end=" ")
    print()

  
  m = len(Y)
  try: n = len(Y[0])
  except TypeError: n = 1
  if frec == 0: frec = m
  imprimeEncabezado(n)
  for i in range(0,m,frec):
   imprimeLinea(X[i],Y[i],n)
  if i != m - 1: imprimeLinea(X[m - 1],Y[m - 1],n)
  
def F(x,y):
  F= np.sin(y)
  return F

x0 = 0
xStop = 0.5
h = 0.01
y0=1

X, Y = eulerint(F, x0, y0, xStop, h)

print("Ejercicio 3: y' = sin(y), y(0) = 1")
imprimeSol(X, Y, 10) 


#EJERCICIO 4 SEC. 7.1


def F4(x, y):
    return y**(1/3)

#inciso A

x0 = 0
xStop = 1
h = 0.1
y0_a = 0.0

X4a, Y4a = eulerint(F4, x0, y0_a, xStop, h)
print("\nEjercicio 4(a): y' = y^{1/3}, y(0) = 0")
imprimeSol(X4a, Y4a, 1)

#inciso b
y0_b = 1e-16

X4b, Y4b = eulerint(F4, x0, y0_b, xStop, h)
print("\nEjercicio 4(b): y' = y^{1/3}, y(0) = 1e-16")
imprimeSol(X4b, Y4b, 1)


#EJERCICIO 3(a) SEC. 8.1

def Run_Kut4(F,x,y,xStop,h):
  def run_kut4(F,x,y,h):
    K0 = h*F(x,y)
    K1 = h*F(x + h/2.0, y + K0/2.0)
    K2 = h*F(x + h/2.0, y + K1/2.0)
    K3 = h*F(x + h, y + K2)
    return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

  X = []
  Y = []
  X.append(x)
  Y.append(y.copy())
  while x < xStop:
    h = min(h,xStop - x)
    y = y + run_kut4(F,x,y,h)
    x = x + h
    X.append(x)
    Y.append(y.copy())
  return np.array(X),np.array(Y)

def imprimeSol(X,Y,frec):
  def imprimeEncabezado(n):
    print("\n x ",end=" ")
    for i in range (n):
      print(" y[",i,"] ",end=" ")
    print()
  def imprimeLinea(x,y,n):
    print("{:13.4e}".format(x),end=" ")
    for i in range (n):
      print("{:13.4e}".format(y[i]),end=" ")
    print() 
  m = len(Y)
  try: n = len(Y[0])
  except TypeError: n = 1
  if frec == 0: frec = m
  imprimeEncabezado(n)
  for i in range(0,m,frec):
    imprimeLinea(X[i],Y[i],n)
  if i != m - 1: imprimeLinea(X[m - 1],Y[m - 1],n)

#Inciso a

def F_a(x, y):
  return np.array([y[1], -np.exp(-y[0])])


y0_0 = 1       # y(0)
y1 = 0.5  # y(1)


def shoot_a(s):
  y_init = np.array([y0_0, s])
  X, Y = Run_Kut4(F_a, 0, y_init, 1, 0.01)
  return Y[-1,0] - y1  #y(1) = 0.5

s1, s2 = -2, 2
for i in range(30):
  sm = (s1 + s2)/2
  fm = shoot_a(sm)
  if abs(fm) < 1e-6: break
  if shoot_a(s1)*fm < 0:
    s2 = sm
  else:
    s1 = sm

y_init = np.array([y0_0, sm])
X, Y = Run_Kut4(F_a, 0, y_init, 1, 0.01)

print(f"\nEstimación de y'(0): {sm:.6f}")
print("Solución para el caso (a):")
imprimeSol(X,Y,10)

plt.plot(X,Y[:,0],label="y(x)")
plt.plot(X,Y[:,1],label="y'(x)")
plt.xlabel("x")
plt.ylabel("Solución")
plt.title("Problema de frontera (a)")
plt.grid()
plt.legend()
plt.show()


#EJERCICIO 3(b) SEC. 8.1

def Run_Kut4(F,x,y,xStop,h):
  def run_kut4(F,x,y,h):
    K0 = h*F(x,y)
    K1 = h*F(x + h/2.0, y + K0/2.0)
    K2 = h*F(x + h/2.0, y + K1/2.0)
    K3 = h*F(x + h, y + K2)
    return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

  X = []
  Y = []
  X.append(x)
  Y.append(y.copy())
  while x < xStop:
    h = min(h,xStop - x)
    y = y + run_kut4(F,x,y,h)
    x = x + h
    X.append(x)
    Y.append(y.copy())
  return np.array(X),np.array(Y)

def imprimeSol(X,Y,frec):
  def imprimeEncabezado(n):
    print("\n x ",end=" ")
    for i in range (n):
      print(" y[",i,"] ",end=" ")
    print()
  def imprimeLinea(x,y,n):
    print("{:13.4e}".format(x),end=" ")
    for i in range (n):
      print("{:13.4e}".format(y[i]),end=" ")
    print() 
  m = len(Y)
  try: n = len(Y[0])
  except TypeError: n = 1
  if frec == 0: frec = m
  imprimeEncabezado(n)
  for i in range(0,m,frec):
    imprimeLinea(X[i],Y[i],n)
  if i != m - 1: imprimeLinea(X[m - 1],Y[m - 1],n)

#Inciso b

def F_b(x, y):
  return np.array([y[1], 4*y**2])

y0_0 = 10       # y(0)
y1 = 0.0  # y'(1)


def shoot_b(s):
  y_init = np.array([y0_0, s])
  X, Y = Run_Kut4(F_b, 0, y_init, 1, 0.01)
  return Y[-1,0] - y1  #y(1) = 0.0

s1, s2 = -2, 2
for i in range(30):
  sm = (s1 + s2)/2
  fm = shoot_a(sm)
  if abs(fm) < 1e-6: break
  if shoot_a(s1)*fm < 0:
    s2 = sm
  else:
    s1 = sm

y_init = np.array([y0_0, sm])
X, Y = Run_Kut4(F_a, 0, y_init, 1, 0.01)

print(f"\nEstimación de y'(0): {sm:.6f}")
print("Solución para el caso (b):")
imprimeSol(X,Y,10)

plt.plot(X,Y[:,0],label="y(x)")
plt.plot(X,Y[:,1],label="y'(x)")
plt.xlabel("x")
plt.ylabel("Solución")
plt.title("Problema de frontera (b)")
plt.grid()
plt.legend()
plt.show()
