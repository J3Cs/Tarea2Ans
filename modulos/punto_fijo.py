import math

#funcion del ejercicio
def f(a,funcion):
    x = symbols('x')
    return funcion.subs(x,a)

#Sacando la primer derivada
def dx(a,funcion):
    
    return f(a,str(diff(eval(funcion),x)))

#Punto Fijo
#Reicibe valores iniciales a y b recibe r valor que esta entre a y b y recibe Error especifico y la funcion despejada en g(x)
def punto_fijo(a,b,r,Es,funcion):
     """
    Parametros:
     a -- primer valor inicial
     b-- Segundo valor}
     r-- valor entre a y b
     Es -- error especifico
     funcion -- la cadena de la funcion despejada (gx)
    """
    ab=f(a,funcion)-a
    ba=f(b,funcion)-b
    Ea=1
    if (ab>0 and ba<0):
        ra=dx(r,funcion)
        if ra<1 :
            while Ea > Es :
                r1=f(r,funcion)
                Ea=abs((r1-r)/r1)*100
                r=r1
        else:
            return "no converge"
    else:
        return "no converge"
    return r