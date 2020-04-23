from sympy import *
import math

x = Symbol('x')
#Funcion del Ejercicio
def f(x,funcion):
    return eval(funcion.replace("x",str(x)))


#Sacando la primer derivada
def dx(a,funcion):
    
    return f(a,str(diff(eval(funcion),x)))

def punto_fijo(r,Es,fx,gx)