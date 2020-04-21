import math
import numpy as np
print ("\nMetodo Trataglia\n")

#Llevar a la forma x^3+ax^2+bx+c=0
p = [6,-17,-5,6]#coeficientes
d =[]
i=0
while True:
    d.append(p[i]/p[0])
    i=i+1
    if (i==4):
        break
a=d[1]
b=d[2]
c=d[3]
#print (a,b,c)
def f(x,a,b,c):
    return (x**3)+(a*x**2)+(b*x)+c
#calcular el signo
def sgn(x):
    if(x<0):
        return -1
    if(x>0):
        return 1
    return 0
#tartaglia
def tartaglia(a,b,c):
    Q=((a*a)-(3*b))*(9**(-1))
    R=((2*(a**3))-(9*a*b)+(27*c))*(54**(-1))
    if((R*2)<(Q**3)):
        ang=math.acos(R/((Q**3)**(0.5)))
        X= -2*(Q**(0.5))*math.cos(ang/3)-(a/3)
        Y= -2*(Q**(0.5))*math.cos(((ang+2*math.pi))/3)-(a/3)
        Z= -2*(Q**(0.5))*math.cos(((ang-2*math.pi))/3)-(a/3)
    else:
        A=-sgn(R)*((abs(R)+((R**2)-Q**3))**(0.5))**(1/3)
        if(A!=0):
            B=Q/A
        else:
            B=0
        X=(A+B)-(a/3)
        Y=(-0.5)*(A+B)-(a/3)+math.sqrt(-1)*((3**(0.5))/2)*(A-B)
        Z=(-0.5)*(A+B)-(a/3)-math.sqrt(-1)*((3**(0.5))/2)*(A-B)
    return [X,Y,Z]

print("#\t\t\tRaiz")
i=0
calcu=tartaglia(a,b,c)
for r in calcu:
    print (str(i),"\t\t",str(r))
    i=i+1
print ("\nLa Raiz es = ", str(r),"\n")  