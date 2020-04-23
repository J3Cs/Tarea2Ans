import math


#Funcion del Ejercicio
def f(x,funcion):
    return eval(funcion.replace("x",str(x)))

#Recibe tres valores iniciales y la cadena de la funcion
def muller(x0,x1,x2,Es,funcion):
    """
    Parametros:
     x0 -- primer valor inicial
     x1 -- Segundo valor
     x2 -- tercer valor
     Es -- error especifico
     funcion -- la cadena de la funcion
    """
    Ea=1

    while Ea>Es:
    
        h0=x1-x0
        h1=x2-x1
        delta0=(f(x1,funcion)-f(x0,funcion))/h0
        delta1=(f(x2,funcion)-f(x1,funcion))/h1
        a=(delta1-delta0)/(h1+h0)
        b=a*h1+delta1
        c=f(x2,funcion)
        if b>0:
            if (b*b-4*a*c)>0:
                xr=x2+(-2*c)/(b+math.sqrt(b*b-4*a*c)) 
            else:
                xr=x2+(-2*c)/(complex(b,math.sqrt(b*b-4*a*c))) 
        else:
            if (b*b-4*a*c)>0:
                xr=x2+(-2*c)/(b-math.sqrt(b*b-4*a*c)) 
            else:
                xr=x2+(-2*c)/(complex(b,-math.sqrt(b*b-4*a*c))) 
        Ea=Abs((xr-x2)/xr)*100
        x0=x1
        x1=x2
        x2=xr
    return x2

