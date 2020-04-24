import math
import sympy 
from Tartaglia import tartaglia

def entreElprimero(coef):
    if(coef[0]!=1):
        num= coef[0]
        for i in range(0,len(coef)):
            coef[i]=coef[i]/num
    return coef

def tartagliaByFerrari(coef):
    coef=entreElprimero(coef)
    a=coef[1]
    b=coef[2]
    c=coef[3]
    p=b-(a**2)/3
    q=c-(a*b)/3+(2*a**3)/27
    k=-(a/3)
    D=(4*p**3+27*q**2)/108
    if D>0:
        A=-(q/2)+math.sqrt((q**2)/4+(p**3)/27)
        B=-(q/2)-math.sqrt((q**2)/4+(p**3)/27)
        x=((A)**(1/3))+((B)**(1/3))+k
    elif D<0:
        ang=math.acos((math.sqrt(27)*q)/(2*p)*math.sqrt(-1*p))
        x=2*math.sqrt(-p/3)*math.cos(ang/3)+k
    else:
        x=2*(-q/2)**(1/3)
    return x
    

def ferrari(coef):
    coef=entreElprimero(coef)
    a=coef[1]
    b=coef[2]
    c=coef[3]
    d=coef[4]
    
    P=(8*b-3*(pow(a,2)))/8
    Q=(8*c-4*a*b+pow(a,3))/8
    R=(256*d-64*a*c+16*pow(a,2)*b-3*pow(a,4))/256

    au=-(P/2)
    bu=(R)
    cu=((4*P*R)-pow(Q,2))/8
    t=tartaglia([1,au,bu,cu])
    U=t[0]
    V=math.sqrt(2*U-P)
    W=Q/(-2*V)
    D=V**2-4*(U-W)
    if(D>0):
        x=[
            ((V+math.sqrt(D))/2-a/4),
            ((V-math.sqrt(D))/2-a/4),
            ((-V+math.sqrt(D))/2-a/4),
            ((-V-math.sqrt(D))/2-a/4)
        ]
    else:
        x=[
            complex(V/2-a/4,abs(D)/2),
            complex(V/2-a/4,-abs(D)/2),
            complex(-V/2-a/4,abs(D)/2),
            complex(-V/2-a/4,-abs(D)/2)
        ]

    return x


