import math

print ("\nMetodo de la Biseccion")

#Funcion del Ejercicio
def f(x):
    return (1.5)-math.log(1+x**2)

rango_inicio = 1
rango_final = 2
cs=3
es=0.5*(10**(2-cs))
Ea=1
print("\nX: \t\t\tError Aprox: ")

while(abs(Ea) > es):
    Xr = (rango_inicio + rango_final) / 2
    Ea = (Xr-rango_inicio)/Xr
    print(Xr,"\t\t",Ea)
    if(f(rango_inicio) * f(Xr) < 0):
        rango_final = Xr
    else:
        rango_inicio = Xr
print ("\nLa Raiz es: ", Xr,"\nErro Aprox: ",Ea,"\n")