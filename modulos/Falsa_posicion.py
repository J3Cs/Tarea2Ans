import math
from sympy import *
#Metodo de la falsa posicion
#Recibe como parametro 2 valores enteros iniciales, el error especifico y la cadena de la funcion ingresada
def falsa_posicion(x1,x2,Es,funcion):
    """
     Devuelve una lista con las posibles raiz de la ecuacio.
     Parametros:
     x1 -- primer valor inicial
     x2 -- Segundo valor
     Es -- error especifico
     funcion -- la cadena de la funcion
    """
    x = symbols('x')
    if (funcion.subs(x, x1)*funcion.subs(x, x2)<0):
        xr=0
        anterior=0
        Ea=1
        while Ea>Es:
            xr = x2 - ((x1-x2) * funcion.subs(x, x2))/( funcion.subs(x, x1) - funcion.subs(x, x2) )

            if funcion.subs(x, x1) * funcion.subs(x, xr) < 0:
                anterior = x2
                x2 = xr
            else:
                x1 = xr

            Ea = abs((xr - anterior) / xr) * 100
        return xr
    else:
        return "no sirve"
    