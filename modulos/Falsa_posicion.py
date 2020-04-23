import math

def f(x,funcion):
    return eval(funcion.replace("x",str(x)))


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
    if (f(x1,funcion)*f(x2,funcion)<0):
        xr=0
        anterior=0
        Ea=1
        while Ea>Es:
            xr = x2 - ((x1-x2) * f(x2,funcion))/( f(x1,funcion) - f(x2,funcion) )

            if f(x1,funcion) * f(xr,funcion) < 0:
                anterior = x2
                x2 = xr
            else:
                x1 = xr

            Ea = abs((xr - anterior) / xr) * 100
        return xr
    else:
        return "no sirve"
    