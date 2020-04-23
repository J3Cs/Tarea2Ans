import math

def f(a,funcion):
    x = symbols('x')
    return funcion.subs(x,a)

def secante(xi,xh,Es,funcion):
    """
     Devuelve una lista con las posibles raiz de la ecuacio.
     Parametros:
     xi -- primer valor inicial
     xh -- Segundo valor
     Es -- error especifico
     funcion -- la cadena de la funcion
    """
    if (f(xi,funcion)*f(xh,funcion)<0):
        Ea=1
        while Ea>Es:
            
            xi1 = xi - (f(xi,funcion)*(xh-xi))/( f(xh,funcion) - f(xi,funcion) )
            Ea = abs((xi1-xi)/xi1) * 100
            xh=xi
            xi=xi1
        return xi
    else:
        return "no existe raiz"


