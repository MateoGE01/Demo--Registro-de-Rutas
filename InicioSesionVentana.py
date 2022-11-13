import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from redimension import * 
from ventanaMapa import mapa
import csv

class login:

    def InicioSesion(self):
        i = False
        placa = self.usuario.get()
        clave = self.password.get()
        with open("PlacasClaves.csv", mode="r") as f:
            reader = csv.reader(f, delimiter = ";")
            for row in reader:#si nunca entra al if entonces i=False, por lo que saldrá el mensaje de error
                if row == [placa, clave]:
                    self.ventana.destroy()
                    mapa()   
                    i = True
            if (i == False):
                messagebox.showerror(message="Un dato es incorrecto",title="Mensaje")        
       
    def __init__(self) -> None:
        self.ventana = tk.Tk()    #creacion de ventana                         
        self.ventana.title('Registro de Viaje')
        self.ventana.geometry('1200x700')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        centrar_ventana(self.ventana,800,500)

        logo =leer_imagen("./imagenes/DonQueso.png", (350, 350))

        # frame_logo panel de la izquierda
        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#3a7ff6')
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='#3a7ff6' )
        label.place(x=0,y=0,relwidth=1, relheight=1)

        #frame_form panel de la derecha
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top será el título
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill a la derecha del logo y debajo del título "Inicio de Sesion"
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        #Escribir la placa
        etiqueta_usuario = tk.Label(frame_form_fill, text="Placa", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        #Escribir la clave
        etiqueta_password = tk.Label(frame_form_fill, text="Clave", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.InicioSesion)
        inicio.pack(fill=tk.X, padx=20,pady=20)

        inicio.bind("<Return>", (lambda event: self.InicioSesion()))


        self.ventana.mainloop()