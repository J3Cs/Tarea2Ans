
import numpy as np
from sympy import *
import math


print ("\nMetodo Newton Raphson")
x = Symbol('x')
#Funcion del Ejercicio
def f(x):
    return (1.5)-math.log(1+x**2)
    

#Sacando la primer derivada
def dx(x):
    return ((2*x)/-((x**2)+1))

#deriv =diff(f(x))
#print (deriv)
#print (dx)
print("\n#","        Raiz","        convergencia","     Error Aprox")

#Valores de el error aceptado,cifras significativas y el maximo de iteraciones permitidas
cs=5
x0=2
es=(0.5*(10**(2-cs)))
imax = 1000

#valores iniciales para el bucle
ea=1
xi=x0
itera=0
while ea > es and itera < imax:
    ea = np.abs(f(xi)/(dx(xi)/xi))
    x1 = xi - f(xi)/dx(xi)
    print('%i   %15.12f   %15.12f   %15.12f' % (itera+1, x1, np.abs(f(xi)/dx(xi)), ea))
    xi = x1
    itera += 1
print ("\nLa raiz es: ", x1,"\nError Aprox: ",ea,"\n")






