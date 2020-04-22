import math
import re
def Horner(func, Es, limitA, limitB, xi):
    fun = func
    Es = Es
    Ea = 1
    xi = xi
    arr = []
    arr1 = []
    R = 0.0
    S = 0.0
    coeficientes = coefs(fun)
    grado = len(coeficientes)-1
    m = math.fabs(coeficientes[0])
    n = math.fabs(coeficientes[grado])
    limitA = limitA
    limitB = limitB
    for t in range(len(coeficientes)):
      if t == 0:
        faPos = coeficientes[t]
        faNeg = coeficientes[t]
        fbPos = coeficientes[t]
        fbNeg = coeficientes[t]
      else:
        faPos = faPos + coeficientes[t]*limitA**t
        faNeg = faNeg + coeficientes[t]*-limitA**t
        fbPos = fbPos + coeficientes[t]*limitB**t
        fbNeg = fbNeg + coeficientes[t]*-limitB**t

    intocable = coeficientes[len(coeficientes)-1]

    if faPos * fbPos < 0:
      for i in range(len(coeficientes), 1, -1):
        if i == len(coeficientes):
          m = intocable*xi
          arr.append(m+coeficientes[i-2])
          pos = 0
        else:
          pos = pos + 1
          m = arr[pos-1]*xi
          arr.append(m+coeficientes[i-2]) 
          R = arr[pos]
       
      for j in range((len(arr)-1)):
        if j == 0:
            m = intocable*xi
            arr1.append(m+arr[j])
        else:
            m = arr1[j-1]*xi
            arr1.append(m+arr[j]) 
            S = arr1[j]
      xi1 = xi - (R/S)
      Ea = math.fabs((xi1-xi)/xi1)*100
      arr = []
      arr1 = []
      R = 0.0
      S = 0.0
      while Ea > Es:
        xi = xi1
        for i in range(len(coeficientes), 1, -1):
          if i == len(coeficientes):
            m = intocable*xi
            arr.append(m+coeficientes[i-2])
            pos = 0
          else:
            pos = pos + 1
            m = arr[pos-1]*xi
            arr.append(m+coeficientes[i-2]) 
            R = arr[pos]
        
        for j in range((len(arr)-1)):
          if j == 0:
            m = intocable*xi
            arr1.append(m+arr[j])
          else:
            m = arr1[j-1]*xi
            arr1.append(m+arr[j]) 
            S = arr1[j]
        xi1 = xi - (R/S)
        Ea = math.fabs((xi1-xi)/xi1)*100

    elif faNeg * fbNeg < 0:
      for i in range(len(coeficientes), 1, -1):
        if i == len(coeficientes):
          m = intocable*xi
          arr.append(m+coeficientes[i-2])
          pos = 0
        else:
          pos = pos + 1
          m = arr[pos-1]*xi
          arr.append(m+coeficientes[i-2]) 
          R = arr[pos]
       
      for j in range((len(arr)-1)):
        if j == 0:
            m = intocable*xi
            arr1.append(m+arr[j])
        else:
            m = arr1[j-1]*xi
            arr1.append(m+arr[j]) 
            S = arr1[j]
      xi1 = xi - (R/S)
      Ea = math.fabs((xi1-xi)/xi1)*100
      arr = []
      arr1 = []
      R = 0.0
      S = 0.0
      while Ea > Es:
        xi = xi1
        print("xi ",xi)
        for i in range(len(coeficientes), 1, -1):
          if i == len(coeficientes):
            m = intocable*xi
            arr.append(m+coeficientes[i-2])
            pos = 0
          else:
            pos = pos + 1
            m = arr[pos-1]*xi
            arr.append(m+coeficientes[i-2]) 
            R = arr[pos]
        
        for j in range((len(arr)-1)):
          if j == 0:
            m = intocable*xi
            arr1.append(m+arr[j])
          else:
            m = arr1[j-1]*xi
            arr1.append(m+arr[j]) 
            S = arr1[j]
        xi1 = xi - (R/S)
        Ea = math.fabs((xi1-xi)/xi1)*100
        
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
Horner("x^3+7x^2+7x-15", 0.05, 0.9375, 2, 0.95)