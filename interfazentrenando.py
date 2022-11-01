from tkinter import *

raiz = Tk()#uso de clase

raiz.title("RacedoEsVegeta")#Titulo de ventana

raiz.iconbitmap("nobitches.ico")#icono de la ventana

"""
Hace que puedas permitir o no al usuario cambiar el ancho o alto
0 = false , no permite
1 = true , permite

resizable(ancho, alto)

----raiz.resizable(0,0)
"""

"""
----raiz.geometry("650x350")  #tamaño predeterminado de la ventana

Sin embargo, la ventana principal al iniciarse se ajusta al frame que tenga adentro,
por lo que es innecesario ponerle un tamaño
"""

raiz.config(bg="black")#el config permite hacer muchas cosas, como el color de la ventana
raiz.config(bd=25)
raiz.config(relief="sunken")
raiz.config(cursor="hand2")


marcoprincipal = Frame()#en este marco se meteran las funcionalidades

marcoprincipal.pack(fill="both", expand="True")#Para meterlo en la ventana principal "raiz", ademas permite hacer otras cosas

marcoprincipal.config(bg ="blue")#Color al frame dentro de la ventana principal

marcoprincipal.config(width=1200, height=700)#Tamaño del frame

marcoprincipal.config(bd=35)#Permitirá luego cambiar el borde del frame --se puede aplicar a "raiz"--

marcoprincipal.config(relief="sunken")#Permite cambiar el borde del frame --se puede aplicar a "raiz"--

marcoprincipal.config(cursor="pirate")#Permite cambiar el cursor sobre el frame --se puede aplicar a "raiz"--


miLabel = Label(marcoprincipal, text="Soy Goku", fg="red", font=("Times New Romans", 18))#Permitira poner imagenes o textos 
miLabel.place(x=720, y=600)#Ubicara "miLabel"
miImagen = PhotoImage(file="Goku.png")#Con esto puedo poner imagenes, hasta ahora lo recomendable es tener en cuenta el tamaño de la imagen
Label(marcoprincipal, image=miImagen).pack(fill="y")



raiz.mainloop()#creacion de ventana(debe estar siempre al final)