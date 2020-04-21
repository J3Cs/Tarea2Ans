import tkinter
from tkinter import ttk

# create main window
master = tkinter.Tk()
master.title("ANS135")
master.configure(bg="#212121")
cmbStyle = ttk.Style()
cmbStyle.theme_create('cmbs',settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#a30030',
                                       'fieldbackground': '#2d000d',
                                       'background': '#ff5486',
                                       'foreground': '#ffffff'
                                       }}})
cmbStyle.theme_use('cmbs')

#Frames para ordenar los componentes
frameEntries = tkinter.Frame(master,bg="#212121")
frameEntries.grid(row=2, column=1)
frGrafica = tkinter.Frame(master,bg="#212121")
frGrafica.grid(row=0, column=0, rowspan=5)
frame = tkinter.Frame(master,bg="#212121")
frame.grid(row=3, column=1)
#--

#Variables
metodos=["Seleccione un metodo", "Biseccion", "Falsa Posicion", "Punto Fijo", "Newton Raphson", "Secante", "Tartaglia", "Ferrari", "Horner", "Müller", "Bairstow"]
#--

#Componentes de la app
tkinter.Label(frameEntries, text="Ingrese la funcion a evaluar", bg="#212121",fg="#ff064f").grid(row=0, column=0)
fn = tkinter.Entry(frameEntries, exportselection=0, bg = "#2d000d", fg = "#FFFFFF")
fn.grid(row=1, column=0)

tkinter.Label(frameEntries, text="Metodos", bg="#212121",fg="#ff064f").grid(row=3, column=0)
cmbMetodos = ttk.Combobox(frameEntries, values=metodos, state="readonly")
cmbMetodos.grid(row=4, column=0)
cmbMetodos.current(0)

tkinter.Label(frameEntries, text="Soluciones", bg="#212121",fg="#ff064f").grid(row=5, column=0)
tkinter.Entry(frameEntries, exportselection=0, bg = "#2d000d", fg = "#FFFFFF", state="readonly").grid(row=6, column=0)


#Area de grafico
tkinter.Label(frGrafica, text="Grafica de la funcion", bg="#212121",fg="#ff064f").grid(row=0, column=2, columnspan=3)
tkinter.Canvas(frGrafica, height=500, width=500, bg="#68001f").grid(row=1,column=2, rowspan=6, columnspan=3)
#--

#Creacion de botones numericos
zero = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="0", activebackground="#E040FB")
uno = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="1", activebackground="#E040FB")
dos = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="2", activebackground="#E040FB")
tres = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="3", activebackground="#E040FB")
cuatro = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="4", activebackground="#E040FB")
cinco = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="5", activebackground="#E040FB")
seis = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="6", activebackground="#E040FB")
siete = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="7", activebackground="#E040FB")
ocho = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="8", activebackground="#E040FB")
nueve = tkinter.Button(frame, bg="#b606ff", fg="#FFFFFF", text="9", activebackground="#E040FB")
#--

#Posicionamiento de los botones numericos
uno.grid(row=7, column=0)
dos.grid(row=7, column=1)
tres.grid(row=7, column=2)
cuatro.grid(row=8, column=0)
cinco.grid(row=8, column=1)
seis.grid(row=8, column=2)
siete.grid(row=9, column=0)
ocho.grid(row=9, column=1)
nueve.grid(row=9, column=2)
zero.grid(row=10, column=1)
#--
#--
master.mainloop()
