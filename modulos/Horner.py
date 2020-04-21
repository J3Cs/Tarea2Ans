import math
import re
def Horner():
    x = symbols('x')
    fun = "x^3+7x^2+7x-15"
    Ea = 0.5*10**2-3
    xi = 0.95
    coeficientes = coefs(fun)
    print(coeficientes)
    grado = len(coeficientes)-1
    m = math.fabs(coeficientes[0])
    n = math.fabs(coeficientes[grado])
    limitA = m/(m+n)
    print(limitA)
    limitB = (n+n)/n
#TODO crear la funcion para evaluar con sympy
#def contruirfunc(coef):
   # for item in range(0, len(coef)-1, 1):
        
#Metodo para obtener los coeficientes de la funcion pasada como String
def coefs(entrada):
  regexp = r"(-?\d*)(x?)(?:(?:\^|\*\*)(\d))?"
  c = {}
  for coef, x, exp in re.findall(regexp, entrada):
    # print(coef, x, exp)
    if not coef and not x:
      continue
    if x and not coef:
      coef = '1'
    if x and coef == "-":
      coef = "-1"
    if x and not exp:
      exp = '1'
    if coef and not x:
      exp = '0'
    exp = ord(exp) & 0x000F
    c[exp] = float(coef)
  grado = max(c)
  coeficientes = [0.0] * (grado+1)
  for g, v in c.items():
    coeficientes[g] = v
  return coeficientes
#--
Horner()