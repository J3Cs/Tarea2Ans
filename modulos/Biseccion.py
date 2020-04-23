import math
#Funcion del Ejercicio
def f(x,funcion):
    return eval(funcion.replace("x",str(x)))
#Recibe dos valores iniciales y la cadena de la funcio
def biseccion(x1,x2,Es,funcion):
    """
    Parametros:
     x1 -- primer valor inicial
     x2 -- Segundo valor
     Es -- error especifico
     funcion -- la cadena de la funcion
    """
    
    Ea = 1
    while(abs(Ea) > Es):
        xr = (x1 + x2) / 2
        Ea = (xr-x1)/xr
        if(f(x1,funcion) * f(xr,funcion) < 0):
            x2 = xr
        else:
            x1= xr
    return xr

