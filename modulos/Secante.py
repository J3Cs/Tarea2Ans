import math

print ("\nMetodo de la Secante")


def f(x):
 return (1.5)-math.log(1+x**2)

# iniciando valores
x0 = 1
x1 = 2
cs=3
es=(0.5*(10**(2-cs)))

#Metodo
print("\n#\t\tX2\t\t\tEa")
itera = 1
condicion = True
while condicion:
     x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
     print(itera,"\t", x2,"\t", f(x2))
     x0 = x1
     x1 = x2
     itera = itera + 1        
     condicion = abs(f(x2)) > es

print("\nLa Raiz es: ", x2,"\nEl Error Aprox: ",abs(f(x2)),"\n")