# -*- coding: utf-8 -*-
import tkinter
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import re
from modulos import bairstown, Biseccion, Falsa_posicion, Horner, muller, Newton, Secante, Tartaglia

# create main window
master = tkinter.Tk()
master.title("ANS135")
master.configure(bg="#212121")
cmbStyle = ttk.Style()
cmbStyle.theme_create('cmbs',settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#607D8B',
                                       'fieldbackground': '#673AB7',
                                       'background': '#757575',
                                       'foreground': '#ffffff'
                                       }}})
cmbStyle.theme_use('cmbs')


#Frames para ordenar los componentes
frameEntries = tkinter.Frame(master,bg="#212121")
frameEntries.grid(row=0, column=1, columnspan=2)
frGrafica = tkinter.Frame(master,bg="#212121")
frGrafica.grid(row=0, column=0, rowspan=5)
frame = tkinter.Frame(master,bg="#212121")
frame.grid(row=1, column=1)
frameFn = tkinter.Frame(master,bg="#212121")
frameFn.grid(row=1, column=2)
#--

#Variables
x = symbols('x') 
metodos=["Seleccione un metodo", "Biseccion", "Falsa Posicion", "Punto Fijo", "Newton Raphson", "Secante", "Tartaglia", "Horner", "Müller", "Bairstow"]
func = tkinter.StringVar()
fig = Figure(figsize=(5,4), dpi=100)
cifras = tkinter.StringVar()
x1 = tkinter.StringVar()
x2 = tkinter.StringVar()
Es = 0.0
raiz = tkinter.StringVar()
funci = 0*x
xi = tkinter.StringVar()
#--

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
def crearfuncion(text):
    coeficient = coefs(text)
    funci = 0*x
    for i in range(len(coeficient)):
      funci = funci + coeficient[i]*x**i   
    return funci
  
#Crea una f(x) a partir de los coeficientes obtenidos del string
def obtener(text):
  if text == "":
    messagebox.showerror(message="Ingrese una funcion para poder graficar")
  else:
    coeficient = coefs(text)
    #t -> rango entre el cual estaran los valores de la grafica
    t = np.arange(-5,5, 0.1)
    fig.clear()
    cadena = 0*t
    for i in range(len(coeficient)):
      cadena = cadena + (coeficient[i]*t**i)
    #Aqui se inserta la funcion a graficar
    fig.add_subplot(111).plot(t, cadena)
    #Aqui se crea la grafica
    tkinter.Label(frGrafica, text="Grafica de la funcion", bg="#212121",fg="#ff064f").grid(row=0, column=2, columnspan=3)
    canvas = FigureCanvasTkAgg(fig, frGrafica)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 6, column = 0, columnspan = 6)
#--
#--
def calcEs(text):
  Es = 0.5*10**(2-int(text))
  
#Obtiene el elemento seleccionado del ComboBox
def cmbSelect(event):
  if cifras.get()=="" or func.get() == "":
    messagebox.showerror(message="Por favor llene los campos correspondientes para realizar el calculo")
    cmbMetodos.current(0)
  elif cmbMetodos.get() == "Biseccion" or cmbMetodos.get() == "Falsa Posicion" or cmbMetodos.get()=="Secante":
    calcEs(cifras.get())
    tkinter.Label(frameEntries, text="Ingrese valor inicial", bg="#212121",fg="#ff064f").grid(row=5, column=0)
    x1e = tkinter.Entry(frameEntries, exportselection=0, textvariable=x1, bg = "#673AB7", fg = "#FFFFFF")
    x1e.grid(row=6, column=0)
    tkinter.Label(frameEntries, text="Ingrese valor final", bg="#212121",fg="#ff064f").grid(row=5, column=1)
    x2e = tkinter.Entry(frameEntries, exportselection=0, textvariable=x2, bg = "#673AB7", fg = "#FFFFFF")
    x2e.grid(row=6, column=1)
    if cmbMetodos.get() == "Biseccion":
      tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(Biseccion.biseccion(int(x1.get()), int(x2.get()), Es, crearfuncion(func.get())))).grid(row=7, column=0, columnspan=2)
    elif cmbMetodos.get() == "Falsa Posicion":
      tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(Falsa_posicion.falsa_posicion(int(x1.get()), int(x2.get()), Es, crearfuncion(func.get())))).grid(row=7, column=0, columnspan=2)
    elif cmbMetodos.get() == "Secante":
      tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(Secante.secante(int(x1.get()), int(x2.get()), Es, crearfuncion(func.get())))).grid(row=7, column=0, columnspan=2)
  elif cmbMetodos.get() == "Horner":
    calcEs(cifras.get())
    limitA = tkinter.StringVar()
    limitB = tkinter.StringVar()
    limits = calcularLimites(coefs(func.get()))
    print(coefs(func.get()))
    limitA.set(limits[0])
    limitB.set(limits[1])
    tkinter.Label(frameEntries, text="Valor inferior de intervalo", bg="#212121",fg="#ff064f").grid(row=5, column=0)
    tkinter.Entry(frameEntries, exportselection=0, textvariable=limitA, bg = "#673AB7", fg = "#FFFFFF").grid(row=6, column=0)
    tkinter.Label(frameEntries, text="Valor superior de intervalo", bg="#212121",fg="#ff064f").grid(row=5, column=1)
    tkinter.Entry(frameEntries, exportselection=0, textvariable=limitB, bg = "#673AB7", fg = "#FFFFFF").grid(row=6, column=1)
    tkinter.Label(frameEntries, text="Ingrese un valor que este dentro del intervalo", bg="#212121",fg="#ff064f").grid(row=7, column=0, columnspan=2)
    tkinter.Entry(frameEntries, exportselection=0, textvariable=xi, bg = "#673AB7", fg = "#FFFFFF").grid(row=8, column=0, columnspan=2)
    tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(Horner.Horner(coefs(func.get()), Es, float(limitA.get()), float(limitB.get()), float(xi.get()) ))).grid(row=9, column=0, columnspan=2)
  elif cmbMetodos.get() == "Newton Raphson":
    calcEs(cifras.get())
    tkinter.Label(frameEntries, text="Ingrese un valor", bg="#212121",fg="#ff064f").grid(row=7, column=0, columnspan=2)
    tkinter.Entry(frameEntries, exportselection=0, textvariable=xi, bg = "#673AB7", fg = "#FFFFFF").grid(row=8, column=0, columnspan=2)
    tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(Newton.newton_rapshon(float(xi.get()), Es, crearfuncion(func.get())))).grid(row=9, column=0, columnspan=2)
  elif cmbMetodos.get() == "Tartaglia":
    calcEs(cifras.get())
    tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(Tartaglia.tartaglia(coefs(func.get())))).grid(row=9, column=0, columnspan=2)
  #elif cmbMetodos.get() == "Ferrari":
    #tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(ferrari.ferrari(coefs(func.get())))).grid(row=9, column=0, columnspan=2)
  elif cmbMetodos.get() == "Bairstow":
    calcEs(cifras.get())
    tkinter.Label(frameEntries, text="Ingrese r0", bg="#212121",fg="#ff064f").grid(row=5, column=0)
    x1e = tkinter.Entry(frameEntries, exportselection=0, textvariable=x1, bg = "#673AB7", fg = "#FFFFFF")
    x1e.grid(row=6, column=0)
    tkinter.Label(frameEntries, text="Ingrese s0", bg="#212121",fg="#ff064f").grid(row=5, column=1)
    x2e = tkinter.Entry(frameEntries, exportselection=0, textvariable=x2, bg = "#673AB7", fg = "#FFFFFF")
    x2e.grid(row=6, column=1)
    tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(bairstown.bairstown(float(x1.get()), float(x2.get()), Es, coefs(func.get()) ))).grid(row=9, column=0, columnspan=2)
  elif cmbMetodos.get() == "Müller":
    calcEs(cifras.get())
    tkinter.Label(frameEntries, text="Ingrese x0", bg="#212121",fg="#ff064f").grid(row=5, column=0)
    x1e = tkinter.Entry(frameEntries, exportselection=0, textvariable=x1, bg = "#673AB7", fg = "#FFFFFF")
    x1e.grid(row=6, column=0)
    tkinter.Label(frameEntries, text="Ingrese x1", bg="#212121",fg="#ff064f").grid(row=5, column=1)
    x2e = tkinter.Entry(frameEntries, exportselection=0, textvariable=x2, bg = "#673AB7", fg = "#FFFFFF")
    x2e.grid(row=6, column=1)
    x3=tkinter.StringVar()
    tkinter.Label(frameEntries, text="Ingrese x2", bg="#212121",fg="#ff064f").grid(row=7, column=0, columnspan=2)
    x3e = tkinter.Entry(frameEntries, exportselection=0, textvariable=x3, bg = "#673AB7", fg = "#FFFFFF")
    x3e.grid(row=8, column=0, columnspan=2)
    tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Calcular", activebackground="#673AB7", command=lambda:calcular(muller.muller(float(x1.get()), float(x2.get()), float(x3.get()), Es, crearfuncion(func.get()) ))).grid(row=9, column=0, columnspan=2)
def calcularLimites(text):
  limits = []
  a = float(text[0])
  b = float(text[len(text)-1])
  limits.append(Abs(a)/(Abs(a)+b))
  limits.append((Abs(b)+b)/Abs(b))
  print(limits)
  return limits

def calcular(fn):
  raiz.set(fn)
#-- 

#Componentes de la app
tkinter.Label(frameEntries, text="Ingrese la funcion a evaluar", bg="#212121",fg="#ff064f").grid(row=0, column=0, columnspan=2)
fn = tkinter.Entry(frameEntries, exportselection=0, textvariable=func, bg = "#673AB7", fg = "#FFFFFF", width=60)
fn.grid(row=1, column=0, columnspan=2)
fn.focus()
tkinter.Button(frameEntries, bg="#b606ff", fg="#FFFFFF", text="Graficar", activebackground="#673AB7", command=lambda:obtener(func.get())).grid(row=2, column=0, columnspan=2)


tkinter.Label(frameEntries, text="Cifras Significativas", bg="#212121",fg="#ff064f").grid(row=3, column=0)
cs = tkinter.Entry(frameEntries, exportselection=0, textvariable=cifras, bg = "#673AB7", fg = "#FFFFFF", width=20)
cs.grid(row=4, column=0)


tkinter.Label(frameEntries, text="Metodos", bg="#212121",fg="#ff064f").grid(row=3, column=1)
cmbMetodos = ttk.Combobox(frameEntries, values=metodos, state="readonly")
cmbMetodos.grid(row=4, column=1)
cmbMetodos.current(0)
cmbMetodos.bind("<<ComboboxSelected>>", cmbSelect)

tkinter.Label(frameEntries, text="Soluciones", bg="#212121",fg="#ff064f").grid(row=10, column=0, columnspan=2)
tkinter.Entry(frameEntries, exportselection=0, disabledbackground = "#2d000d", textvariable=raiz, fg = "#FFFFFF", state="disabled", width=60).grid(row=11, column=0, columnspan=2)


#Area de grafico
#Aqui se crea el area para graficar
tkinter.Label(frGrafica, text="Grafica de la funcion", bg="#212121",fg="#ff064f").grid(row=0, column=2, columnspan=3)
canvas = FigureCanvasTkAgg(fig, frGrafica)
canvas.get_tk_widget().grid(row = 6, column = 0, columnspan = 6)

#Escribe en el Entry llamado fn
def escribir(text):
    func.set(func.get()+text.cget("text"))

#--
#Creacion de botones numericos
zero = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="0", activebackground="#673AB7", command=lambda:escribir(zero))
uno = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="1", activebackground="#673AB7", command=lambda:escribir(uno))
dos = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="2", activebackground="#673AB7", command=lambda:escribir(dos))
tres = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="3", activebackground="#673AB7", command=lambda:escribir(tres))
cuatro = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="4", activebackground="#673AB7", command=lambda:escribir(cuatro))
cinco = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="5", activebackground="#673AB7", command=lambda:escribir(cinco))
seis = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="6", activebackground="#673AB7", command=lambda:escribir(seis))
siete = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="7", activebackground="#673AB7", command=lambda:escribir(siete))
ocho = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="8", activebackground="#673AB7", command=lambda:escribir(ocho))
nueve = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="9", activebackground="#673AB7", command=lambda:escribir(nueve))
#--

#Creacion de botones de funciones
sen = tkinter.Button(frameFn, bg="#b606ff", fg="#FFFFFF", text="Sen(x)", activebackground="#673AB7", width=6, command=lambda:escribir(sen))
cos = tkinter.Button(frameFn, bg="#b606ff", fg="#FFFFFF", text="Cos(x)", activebackground="#673AB7", width=6, command=lambda:escribir(cos))
tan = tkinter.Button(frameFn, bg="#b606ff", fg="#FFFFFF", text="Tan(x)", activebackground="#673AB7", width=6, command=lambda:escribir(tan))
e = tkinter.Button(frameFn, bg="#b606ff", fg="#FFFFFF", text="e^(x)", activebackground="#673AB7", width=6, command=lambda:escribir(e))
ln = tkinter.Button(frameFn, bg="#b606ff", fg="#FFFFFF", text="Ln(x)", activebackground="#673AB7", width=6, command=lambda:escribir(ln))
log = tkinter.Button(frameFn, bg="#b606ff", fg="#FFFFFF", text="Log(x)", activebackground="#673AB7", width=6, command=lambda:escribir(log))
#--
#Posicionamiento de los botones numericos
uno.grid(row=0, column=0)
dos.grid(row=0, column=1)
tres.grid(row=0, column=2)
cuatro.grid(row=1, column=0)
cinco.grid(row=1, column=1)
seis.grid(row=1, column=2)
siete.grid(row=2, column=0)
ocho.grid(row=2, column=1)
nueve.grid(row=2, column=2)
zero.grid(row=3, column=1)
#--
#Posicionamiento de los botones de funciones
sen.grid(row=0, column=0)
cos.grid(row=0, column=1)
tan.grid(row=0, column=2)
e.grid(row=1, column=0)
ln.grid(row=1, column=1)
log.grid(row=1, column=2)
#--

#--
master.mainloop()