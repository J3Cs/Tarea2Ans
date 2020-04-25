import math
import sympy as sym
from sympy import *
import numpy as np
#Funcion del Ejercicio
#def f(x,funcion):
 #   return eval(funcion.replace("x",str(x)))

#Recibe dos valores iniciales y la cadena de la funcio
def biseccion(x1,x2,Es,funcion):
    x = symbols('x')
    """
    Parametros:
     x1 -- primer valor inicial
     x2 -- Segundo valor
     Es -- error especifico
     funcion -- la cadena de la funcion
    """
    if (funcion.subs(x, x1)*funcion.subs(x, x2)<0):
        xr=0
        Ea = 1
        while(abs(Ea) > Es):
            anterior=xr
            xr = (x1 + x2) / 2
            Ea = ((xr-anterior)/xr)*100
            if(funcion.subs(x, x1)) * (funcion.subs(x, xr)) < 0:
                x2 = xr
            else:
                x1= xr
        return xr
    else:
        return "no hay raiz"


