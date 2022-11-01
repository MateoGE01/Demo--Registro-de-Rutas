from cgitb import text
from distutils.command.config import config
from tkinter import *

ventana = Tk()
ventana.title("Registro")
#-----aqui ira el icono-----#

ventana.config(bg="black")#el config permite hacer muchas cosas, como el color de la ventana
ventana.config(bd=3)
ventana.config(relief="sunken")
ventana.config(cursor="hand2")

marcoprincipal = Frame()
marcoprincipal.pack(fill="both", expand="True")
marcoprincipal.config(bg ="green",width=1200, height=700,bd=5,relief="sunken",cursor="pirate")

minombre=StringVar()
apellido=StringVar()
Placa = StringVar()
#-----------------------------------Cuadros de textos----------------------------------#
cuadroNombre=Entry(marcoprincipal, textvariable=minombre)
cuadroNombre.grid(row=0, column=1,padx=3, pady=3)# (fila, columna) son los parametros
cuadroNombre.config(fg="red", justify="center")#fg: color de texto, justify: posicion de texto

cuadroApellido=Entry(marcoprincipal, textvariable=apellido)
cuadroApellido.grid(row=1, column=1,padx=3, pady=3)#1 padx y pady permite que haya espacio para el elemento en los cuatro lados
cuadroApellido.config(fg="red", justify="center")   #2 padx es para horizontal y pady es para vertical
cuadroPlaca=Entry(marcoprincipal, textvariable=Placa)                   
cuadroPlaca.grid(row=2, column=1,padx=3, pady=3)
cuadroPlaca.config(fg="red", justify="center")
cuadroContraseña=Entry(marcoprincipal)  ####referencia para contraseña####
cuadroContraseña.grid(row=3, column=1,padx=3, pady=3)
cuadroContraseña.config(fg="red", justify="center", show="*")#show permite cambiar el texto mostrado en el cuadro de texto
                                                                #por ejemplo, si escribo "Hola" lo que irá apareciendo en el cuadro de texto es "****"
TextoComentario=Text(marcoprincipal, width=16, height=5)                   
TextoComentario.grid(row=4, column=1,padx=3, pady=3)
#-----------------------------Barra de movimiento------------------------------------#
scrollVert=Scrollbar(marcoprincipal, command=TextoComentario.yview)#Scrollbar(), la barra de subir o bajar
scrollVert.grid(row=4, column=2, sticky="nsew")#sticky="nsew" permite que el boton de la scrollbar se pueda mover con el mouse

TextoComentario.config(yscrollcommand=scrollVert.set)#aparecera el boton de lo haya dejado y al mismo tiempo aparecera si hay mucho texto

#---------------------------Textos----------------------------#
nombreLabel=Label(# A frame that is used to contain the widgets.
marcoprincipal, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e",padx=3, pady=3)#sticky sirve para mover el texto, se usa la inicial de los puntos cardinales en ingles
ApellidoLabel=Label(marcoprincipal, text="Apellido:")
ApellidoLabel.grid(row=1, column=0, sticky="e",padx=3, pady=3)
PlacaLabel=Label(marcoprincipal, text="Placa:")
PlacaLabel.grid(row=2, column=0, sticky="e",padx=3, pady=3)
ContraseñaLabel=Label(marcoprincipal, text="Contraseña:")
ContraseñaLabel.grid(row=3, column=0, sticky="e",padx=3, pady=3)
ComentarioLabel=Label(marcoprincipal, text="Comentario:")
ComentarioLabel.grid(row=4, column=0, sticky="e",padx=3, pady=3)

def codigoBoton():
    minombre.set("Mateo")
    apellido.set("Guerrero Escobar")
    Placa.set("TKM341")

botonEnvio=Button(ventana, text="Enviar", command=codigoBoton)
botonEnvio.pack()

ventana.mainloop()