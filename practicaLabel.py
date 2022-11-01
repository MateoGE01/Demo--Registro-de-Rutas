from logging import root
from tkinter import *

principal = Tk()
principal.title("SIU")

marcoprincipal = Frame(principal, width=1200, height=700)
marcoprincipal.pack()

miLabel = Label(marcoprincipal, text="Goku", fg="red", font=("Times New Romans", 18))#Permitira poner imagenes o textos 
miLabel.place(x=250, y=200)#Ubicara "miLabel"

otrolabel = Label(marcoprincipal, text="Manzanita")
otrolabel.place(x=100, y=250)

miImagen = PhotoImage(file="Gokusan.png")#Con esto puedo poner imagenes
Label(marcoprincipal, image=miImagen).place(x=1, y=1)

principal.mainloop()
