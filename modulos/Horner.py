import math
import re

def horner(x0,r0,s0):
	return x0-(r0/s0)


def simpleDivi(raiz,coef):
  x=[coef[0]]
  for i in range(1,len(coef)):
    x.append((coef[i])+(x[i-1]*raiz))
  return x

def entreElprimero(coef):
    if(coef[0]!=1):
        num= coef[0]
        for i in range(0,len(coef)):
            coef[i]=coef[i]/num
    return coef

def Horner(coef, Es, x0):
  Ea = 1
  coef=entreElprimero(coef)
  r=simpleDivi(x0,coef)
  s=simpleDivi(x0,r)
  hor=horner(x0,r[len(r)-1],s[len(s)-2])
  Ea=abs((x0-hor)/hor)*100

  while Ea>Es:
    x0=hor
    r=simpleDivi(coef,x0)
    s=simpleDivi(r,x0)
    hor=horner(x0,r[len(r)-1],s[len(s)-2])
    Ea=abs((x0-hor)/hor)*100

  return hor

c=[2,-4,-3,16,-20]

print(Horner(c,0.05,1))
