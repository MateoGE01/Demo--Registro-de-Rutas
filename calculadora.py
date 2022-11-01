from tkinter import *
from tokenize import String

ventana=Tk()

marcoprincipal= Frame(ventana)
marcoprincipal.pack()
#--------------------------Pantalla-------------------------------------#
numeroPantalla=StringVar()

pantalla=Entry(marcoprincipal,textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#--------------------pulsaciones---------------------------------------------#
def numeroPulsado():

    numeroPantalla.set(numeroPantalla.get()+"4")


#--------------------fila 1---------------------------------------------#

boton7=Button(marcoprincipal, text="7", width=3)
boton7.grid(row=2,column=1)
boton8=Button(marcoprincipal, text="8", width=3)
boton8.grid(row=2,column=2)
boton9=Button(marcoprincipal, text="9", width=3)
boton9.grid(row=2,column=3)
botonDiv=Button(marcoprincipal, text="/", width=3)
botonDiv.grid(row=2,column=4)

#--------------------fila 2---------------------------------------------#

boton4=Button(marcoprincipal, text="4", width=3)
boton4.grid(row=3,column=1)
boton5=Button(marcoprincipal, text="5", width=3)
boton5.grid(row=3,column=2)
boton6=Button(marcoprincipal, text="6", width=3)
boton6.grid(row=3,column=3)
botonMult=Button(marcoprincipal, text="x", width=3)
botonMult.grid(row=3,column=4)

#--------------------fila 3---------------------------------------------#

boton1=Button(marcoprincipal, text="1", width=3)
boton1.grid(row=4,column=1)
boton2=Button(marcoprincipal, text="2", width=3)
boton2.grid(row=4,column=2)
boton3=Button(marcoprincipal, text="3", width=3)
boton3.grid(row=4,column=3)
botonRest=Button(marcoprincipal, text="-", width=3)
botonRest.grid(row=4,column=4)

#--------------------fila 4---------------------------------------------#

boton0=Button(marcoprincipal, text="0", width=3)
boton0.grid(row=5,column=1)
botonComa=Button(marcoprincipal, text=",", width=3)
botonComa.grid(row=5,column=2)
botonIgual=Button(marcoprincipal, text="=", width=3)
botonIgual.grid(row=5,column=3)
botonSum=Button(marcoprincipal, text="+", width=3)
botonSum.grid(row=5,column=4)


ventana.mainloop()