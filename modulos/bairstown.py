import math

#Funcion para la doble division sintetica
def dobledivi(r0,s0,coef):
    x=[]
    x.append(coef[0])
    for i in range(1,len(coef)):
        if i==1:
            x.append((coef[i])+(x[i-1]*r0))
        else:
            x.append((coef[i])+(x[i-1]*r0)+(x[i-2]*s0))
    return x
#Funcion para la division sintetica simple
def simpleDivi(raiz,coef):
    
    x=[coef[0]]
    for i in range(1,len(coef)):
        
            x.append((coef[i])+(x[i-1]*raiz))
    return x

#coef es una lista de coeficientes
def bairstown(r0,s0,Es,coef):
    """
     Devuelve una lista con las posibles raiz de la ecuacio.
     Parametros:
     r0 -- Es el valor inicial de r0
     s0 -- Es el valor inicial de S0
     coef -- es la lista de los coeficientes de la ecuacion
    """
    
    while len(coef)>3:
        Ear=0
        Eas=0
        b=dobledivi(r0,s0,coef)
        c=dobledivi(r0,s0,b)
        c.remove(c[len(c)-1])
        b1=b[len(b)-2]
        b0=b[len(b)-1] 
        c3=c[len(c)-3]
        c2=c[len(c)-2]
        c1=c[len(c)-1]
        x=[]
        deltaR = (-c3 * b0 + c2 * b1) / (c1 * c3 - c2 ** 2)
        deltaS = (-b1 - (c2 * deltaR)) / c3

        r = r0 + deltaR     
        s = s0 + deltaS

        Ear = (deltaR / r) * 100
        Eas = (deltaS / s) * 100
        iteracion=1
        while Ear > Es or Eas > Es :
            r0=r
            s0=s
            b=dobledivi(r0,s0,coef)
            c=dobledivi(r0,s0,b)
            c.remove(c[len(c)-1])
            b1=b[len(b)-2]
            b0=b[len(b)-1] 
            c3=c[len(c)-3]
            c2=c[len(c)-2]
            c1=c[len(c)-1]

            deltaR = (-c3 * b0 + c2 * b1) / (c1 * c3 - c2 ** 2)
            deltaS = (-b1 - (c2 * deltaR)) / c3

            r = r0 + deltaR
            s = s0 + deltaS
            
            Ear = abs((deltaR / r) * 100)
            Eas = abs((deltaS / s) * 100)
        r0=r
        s0=s 
        if (r**2 + 4 * s)<0:
          x.append(complex(r/2,(-1*(r**2 + 4 * s)/2)))
          x.append(complex(r/2,-(-1*(r**2 + 4 * s)/2)))
          coef=[0]
        else:
            x.append((r + math.sqrt(r**2 + 4 * s)) / 2)
            x.append((r - math.sqrt(r**2 + 4 * s)) / 2)       
            coef=simpleDivi(x[len(x)-2],coef)
            coef.remove(coef[len(coef)-1])
            coef=simpleDivi(x[len(x)-1],coef)
            coef.remove(coef[len(coef)-1])


            if (coef[1]**2-4*coef[0]*coef[2])<0:
                x.append(complex(-coef[1]/2,(-1*(coef[1]**2 - 4*coef[0]*coef[2])/2)))
                x.append(complex(-coef[1]/2,-(-1*(coef[1]**2 - 4*coef[0]*coef[2])/2)))

    return x
