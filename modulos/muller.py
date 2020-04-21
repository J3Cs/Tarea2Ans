from sys import argv
print ("\nMetodo Muller\n")

def f(x):
    return (x**7)-(x**5)+(8*x**4)-(8*x**3)-(x**2)+(x)-9
    
#valores iniciales
p0 = 0
p1 = 1
p2 = 1.5
cs=5
es=0.5*(10**(2-cs))

#Evaluando los puntos
fp0 = f(p0)
fp1 = f(p1)
fp2 = f(p2)

print("Las raices estimadas son: ")
print("cuando f(",p0,") = ",fp0)
print("cuando f(",p1,") = ",fp1)
print("cuando f(",p2,") = ",fp2)
print("\n#\t\tf(x)\t\t\t")
itera = 0
print (itera,"\t\t",p0,"\t\t\t",fp0)
fp3 = 1e9


while itera<100 and abs(fp3) >= es:
    fp0 = f(p0)
    fp1 = f(p1)
    fp2 = f(p2)

   
    o = fp1-fp2
    n = fp0-fp2
    s = p1-p2
    r = p0-p2
    det = r*s*(p0-p1)
    a = (s*n-r*o)/det
    b = ((r**2)*o-(s**2)*n)/det
    c = fp2
    itera += 1

    
    x1 = (-2*c)/(b+(b**2-4*a*c)**.5)
    x2 = (-2*c)/(b-(b**2-4*a*c)**.5)

    if b>0:
        p3 = p2+x1
    else:
        p3 = p2+x2

    fp3=f(p3)
    print (itera,"\t",p3,"\t",fp3)
    p2 = p3   

print ("\nLa Raiz es = ", p3,"\n")     

