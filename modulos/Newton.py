from sympy import *
import math

x = symbols('x')
#Funcion del Ejercicio
def f(a,funcion):
    return funcion.subs(x,a)

#Sacando la primer derivada
def dx(a,funcion):
    fprima=diff(funcion,x)
    return f(a,fprima)

#Sacando la segunda derivada
def dxx(a,funcion):
    fprima=diff(funcion,x,x)
    return f(a,fprima)

def newton_rapshon(xi,Es,funcion):
    #valores iniciales para el bucle
    """
    Parametros:
     xi -- primer valor inicial
     Es -- error especifico
     funcion -- la cadena de la funcion
    """
    
    if(abs((f(xi,funcion)*(dxx(xi,funcion))/(dx(xi,funcion)**2)))<1):
        Ea=1
        while Ea > Es :
            
            x1 = xi - f(xi,funcion)/dx(xi,funcion)
            xi = x1
            Ea = abs(f(xi,funcion)/(dx(xi,funcion)/xi))
        return x1
    else:
        return "No converge en ese punto"