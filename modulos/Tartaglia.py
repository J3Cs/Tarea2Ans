import math
import numpy as np

#tartaglia 
#Recibe como parametro un array 
def tartaglia(coeficientes):

    w=coeficientes[0]
    a=coeficientes[1]
    b=coeficientes[2]
    c=coeficientes[3]
    if (w<0 or w>1):
        a=a/w
        b=b/w
        c=c/w
    H=(3*b-a*a)/9
    
    G=((-9)*a*b+27*c+2*(a**3))/54
    D=G*G+H**3
    if(D<0):
        ang=math.acos(-G/(math.sqrt((-H**3))))
        X= 2*(H**(0.5))*math.cos(ang/3)-(a/3)
        Y= 2*(H**(0.5))*math.cos(((ang+2*math.pi))/3)-(a/3)
        Z= 2*(H**(0.5))*math.cos(((ang-2*math.pi))/3)-(a/3)
    elif D==0:
            p=3*H
            q=2*G
            X=(-3*q)/(2*p)-a/3
            Y=(-4*(p*p))/(9*q)-a/3
            Z=(-4*(p*p))/(9*q)-a/3
    else:
        if (-G+math.sqrt(D))<0:
            p=-1*(abs(-G+math.sqrt(D)))**(1/3)
        else:
            p=((-G+math.sqrt(D)))**(1/3)
        if (-G-math.sqrt(D))<0:
            q=-1*(abs(-G-math.sqrt(D)))**(1/3)
            p=((-G+math.sqrt(D)))**(1/3)
        if (-G-math.sqrt(D))<0:
            q=-1*(abs(-G-math.sqrt(D)))**(1/3)
        else:
            q=((-G-math.sqrt(D)))**(1/3)
        X=(p+q)-(a/3)
        Y=complex(-(p+q)/2-(a/3),(p-q)*(math.sqrt(3)/2))
        Z=complex(-(p+q)/2-(a/3),-(p-q)*(math.sqrt(3)/2))
    return [X,Y,Z]
