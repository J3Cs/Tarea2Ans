import math
import re
def Horner(func, Es, limitA, limitB, xi):
    Ea = 1
    xi = xi
    xi1 = 0
    arr = []
    arr1 = []
    R = 0.0
    S = 0.0
    coeficientes = func
    print(func)
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
    return xi1
