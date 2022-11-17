from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from redimension import * 
import csv
from Clases import *
from tkintermapview import *
import time


#Ventana de inicio de sesión principal
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
                    if(self.iteracion == True):
                        rutitas()  
                    i = True
            if (i == False):
                messagebox.showerror(message="Parece que un dato no cuadra🤔",title="Datos no concuerdan")
        
         
       
    def __init__(self, titulo, colorletra, iteracion: bool) -> None:
        self.iteracion = iteracion
        self.ventana = Tk()    #creacion de ventana                         
        self.ventana.title('Inicio de Sesión')
        self.ventana.geometry('800x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.iconbitmap("./imagenes/LogoGuide.ico")
        self.ventana.resizable(width=0, height=0) 
        self.titulo = titulo
        self.colorletra = colorletra       
        centrar_ventana(self.ventana,800,600)

        self.logo =leer_imagen("./imagenes/LogoOOP.png", (400, 130))

        # frame_logo panel de la izquierda
        self.frame_logo = Frame(self.ventana, bd=0, width=400, relief=SOLID, padx=10, pady=10,bg='#b9ea83')
        self.frame_logo.pack(side="left",expand=NO,fill=BOTH)
        self.label = Label( self.frame_logo, image=self.logo,bg='#b9ea83' )
        self.label.place(x=0,y=0,relwidth=1, relheight=1)

        #frame_form panel de la derecha
        self.frame_form = Frame(self.ventana, bd=0, relief=SOLID, bg='#fcfcfc')
        self.frame_form.pack(side="right",expand=YES,fill=BOTH)
        #frame_form
        
        #frame_form_top será el título
        self.frame_form_top = Frame(self.frame_form,height = 50, bd=0, relief=SOLID,bg='black')
        self.frame_form_top.pack(side="top",fill=X)
        self.title = Label(self.frame_form_top, text=self.titulo, font=('Times', 30), fg=self.colorletra,bg='#fcfcfc',pady=50)
        self.title.pack(expand=YES,fill=BOTH)
        #end frame_form_top

        #frame_form_fill a la derecha del logo y debajo del título "Inicio de Sesion"
        self.frame_form_fill = Frame(self.frame_form,height = 2,  bd=0, relief=SOLID,bg='#fcfcfc')
        self.frame_form_fill.pack(side="bottom",expand=YES,fill=BOTH)

        #Escribir la placa
        self.etiqueta_usuario = Label(self.frame_form_fill, text="Placa", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        self.etiqueta_usuario.pack(fill=X, padx=20,pady=5)
        self.usuario = ttk.Entry(self.frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=X, padx=20,pady=10)

        #Escribir la clave
        self.etiqueta_password = Label(self.frame_form_fill, text="Clave", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        self.etiqueta_password.pack(fill=X, padx=20,pady=5)
        self.password = ttk.Entry(self.frame_form_fill, font=('Times', 14))
        self.password.pack(fill=X, padx=20,pady=10)
        self.password.config(show="*")

        self.inicio = Button(self.frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.InicioSesion)
        
        self.inicio.pack(fill=X, padx=20,pady=20)

        self.inicio.bind("<Return>", (lambda event: self.InicioSesion()))

        self.ventana.mainloop()
                       
#Ventana con las rutas posibles
class rutitas:

    def EleccionRutas(self):
        try:
            Eleccion = int(self.usuario.get())     
            if Eleccion  >=1 and Eleccion <=2:
                self.ventana.destroy()
                mapa(Eleccion)
            else:
                messagebox.showerror(message="Parece que un dato no cuadra🤔",title="Datos no concuerdan")  
        except:
            messagebox.showerror(message="Parece que un dato no cuadra🤔",title="Datos no concuerdan")
        
                        
       
    def __init__(self) -> None:
        self.ventana = Tk()    #creacion de ventana                         
        self.ventana.title('Registro de Viaje')
        self.ventana.geometry('800x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.iconbitmap("./imagenes/LogoGuide.ico")
        self.ventana.resizable(width=0, height=0)    
        centrar_ventana(self.ventana,800,600)

        self.logo =leer_imagen("./imagenes/LogoOOP.png", (300, 130))

        # frame_logo panel de la izquierda
        frame_logo = Frame(self.ventana, bd=0, width=300, relief=SOLID, padx=10, pady=10,bg='#b9ea83')
        frame_logo.pack(side="left",expand=NO,fill=BOTH)
        label = Label( frame_logo, image=self.logo,bg='#b9ea83' )
        label.place(x=0,y=0,relwidth=1, relheight=1)

        #frame_form panel de la derecha
        frame_form = Frame(self.ventana, bd=0, relief=SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=YES,fill=BOTH)
        #frame_form
        
        #frame_form_top será el título
        frame_form_top = Frame(frame_form,height = 50, bd=0, relief=SOLID,bg='black')
        frame_form_top.pack(side="top",fill=X)
        title = Label(frame_form_top, text="Rutas",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=20)
        title.pack(expand=YES,fill=BOTH)
        #end frame_form_top

        #frame_form_fill a la derecha del logo y debajo del título "Inicio de Sesion"
        frame_form_fill = Frame(frame_form,height = 50,  bd=0, relief=SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=YES,fill=BOTH)


        inforuta1 = Label(frame_form_fill, text="1: Terminal➜Estadio➜Caribe verde➜Uni Atlantico", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        inforuta1.pack(fill=X, padx=20,pady=5)
        inforuta2 = Label(frame_form_fill, text="2: Terminal➜Camino murillo➜Puente murillo➜Malecon", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        inforuta2.pack(fill=X, padx=20,pady=5)

        #Botón para ver la ruta
        inicio = Button(frame_form_fill,text="Ver ruta",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.EleccionRutas)
        inicio.pack(side="bottom",fill=X, padx=20,pady=20)

        #Pedir al usuario cual ruta desea ver       

        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(side="bottom", fill=X, padx=20,pady=10)
        etiqueta_usuario = Label(frame_form_fill, text="Ruta deseada", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(side="bottom", fill=X, padx=20,pady=5)

        self.ventana.mainloop()

class estadisticas:
                                      
    def __init__(self, horas_llegada, distancias, hora_ideal, hora_salida, estaciones, i) -> None:
        self.estaciones = estaciones
        self.hora_salida = hora_salida
        self.horas_llegada = horas_llegada
        self.distancia = distancias
        self.hora_ideal = hora_ideal
        self.ventana = Tk()    #creacion de ventana                         
        self.ventana.title('Registro de Viaje')
        self.ventana.geometry('800x600')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.iconbitmap("./imagenes/LogoGuide.ico")
        self.ventana.resizable(width=0, height=0)    
        centrar_ventana(self.ventana,800,600)

        self.logo =leer_imagen("./imagenes/LogoOOP.png", (400, 130))

        # frame_logo panel de la izquierda
        self.frame_logo = Frame(self.ventana, bd=0, width=300, relief=SOLID, padx=10, pady=10,bg='#b9ea83')
        self.frame_logo.pack(side="left",expand=NO,fill=BOTH)
        self.label = Label( self.frame_logo, image=self.logo,bg='#b9ea83' )
        self.label.place(x=0,y=0,relwidth=1, relheight=1)

        #frame_form panel de la derecha
        self.frame_form = Frame(self.ventana, bd=0, relief=SOLID, bg='#fcfcfc')
        self.frame_form.pack(side="right",expand=YES,fill=BOTH)
        #frame_form
        
        #frame_form_top será el título
        self.frame_form_top = Frame(self.frame_form,height = 50, bd=0, relief=SOLID,bg='black')
        self.frame_form_top.pack(side="top",fill=X)
        self.title = Label(self.frame_form_top, text="Estadisticas",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=20)
        self.title.pack(expand=YES,fill=BOTH)
        #end frame_form_top

        #frame_form_fill a la derecha del logo y debajo del título "Inicio de Sesion"
        self.frame_form_fill = Frame(self.frame_form,height = 50,  bd=0, relief=SOLID,bg='#fcfcfc')
        self.frame_form_fill.pack(side="bottom",expand=YES,fill=BOTH)


        
        
        hora_real = time.strftime("%H:%M:%p") 
        horas_reales = int(hora_real[0]+hora_real[1])
        horas_ideales = int(self.hora_ideal[0]+self.hora_ideal[1])
        hora_real_min = int(hora_real[3]+hora_real[4])
        horas_ideales_min = int(self.hora_ideal[3]+self.hora_ideal[4])
        velocidad_prom =  self.velocidad(horas_reales, hora_real_min)

        if(horas_reales == horas_ideales):
            if(hora_real_min == horas_ideales_min):
                texto = "Un trabajo verdaremente PERFECTO"
            elif(hora_real_min > horas_ideales_min):
                texto = "No te preocupes un retraso nos pasa a todos 😉"
            else:
                texto = "Mas despacio rayo ⚡"
        elif(horas_reales > horas_ideales):
            texto = "No te preocupes un retraso nos pasa a todos 😉" 
        else:
                texto = "Mas despacio rayo ⚡"

    

        recordatorio = ""
        inforuta1 = Label(self.frame_form_fill, text=texto, font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        inforuta1.pack(fill=X, padx=20,pady=5)
        if(i == 0):
            recordatorio = f"Recuerde que debe estar en: \n {self.estaciones[1]} a las: {self.horas_llegada[1]} \n {self.estaciones[2]} a las: {self.horas_llegada[2]}"
        elif(i == 1):
            recordatorio = f"Recuerde que debe estar en: \n {self.estaciones[2]} a las: {self.horas_llegada[2]}"
        inforuta2 = Label(self.frame_form_fill,
        text=f"Hora de llegada: \n  Ideal: {self.hora_ideal} \n Real: {hora_real} \n Velocidad promedio: {velocidad_prom} km/h \n {recordatorio}",
        font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        inforuta2.pack(fill=X, padx=20,pady=5)
        
        self.inicio = Button(self.frame_form_fill,text="Ver ruta",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.ventana.destroy)
        self.inicio.pack(side="bottom",fill=X, padx=20,pady=20)
        self.ventana.mainloop()

    def velocidad(self,hora_llegada, min_llegada):
        try:    
            distancia = float(self.distancia[0]+self.distancia[1])
            horas_salida = float(self.hora_salida[0]+self.hora_salida[1])
            min_salida = float(self.hora_salida[3]+self.hora_salida[4])
            if(hora_llegada == horas_salida):
                tiempo = min_llegada - min_salida
            else:
                diferencia_horas = hora_llegada - horas_salida
                if(diferencia_horas == 1):
                    tiempo = (min_llegada - min_salida) + 60
                else:
                    tiempo = (diferencia_horas-1)*60 + (min_llegada - min_salida) + 60
            
            return (distancia/(tiempo/60))
        except:
            return "∞"


#Ventana del mapa
class mapa:  

    def __init__(self, opcion): 
        #Creación de variables
        self.opcion = opcion      
        self.origen = "Terminal"
        self.origen_latitud = "10.910700"
        self.origen_longitud = "-74.795472"
        self.estaciones = []
        self.estaciones_latitudes =[]
        self.estaciones_longitudes = []
        self.horas_llegada = []
        self.distancias = []
        self.tiempos = []

        self.mapaset_latitud= None
        self.mapaset_longitud= None
        self.zoom = None    
                  
        self.opciones()
        print(len(self.estaciones))

        
        ruta = Ruta()
        ruta.agregar(self.origen, self.origen_latitud+"%2C"+self.origen_longitud)

        for i in range(len(self.estaciones)): 
            ruta.agregar(self.estaciones[i], self.estaciones_latitudes[i]+"%2C"+self.estaciones_longitudes[i])
        ruta.tiempos_ideales()
        ruta.sumar_horas()
        
        for i in range(len(self.estaciones)): 
            self.tiempos.append(ruta.tiempos[i])
            self.distancias.append(ruta.distancias[i])
            self.horas_llegada.append(ruta.horas_llegada[i])
        self.horas_llegada.append(ruta.horas_llegada[i+1])
        
        
        #Creación de la ventana
        self.VentanaPrin = Tk()
        self.VentanaPrin.geometry("1200x700")
        self.VentanaPrin.title("Mapita")
        self.VentanaPrin.iconbitmap("./imagenes/LogoGuide.ico")
        
        #Creación del frame y el mapa contenido en la misma
        self.ventana_mapa = TkinterMapView(self.VentanaPrin, width=600, height=400, corner_radius=0)        
        self.ventana_mapa.pack(fill="both", expand=True)
        self.ventana_mapa.set_position(self.mapaset_latitud, self.mapaset_longitud)
        self.ventana_mapa.set_zoom(zoom=self.zoom)
       
        #Botones debajo del mapa
        Regresar = Button(self.VentanaPrin, text="Volver a elegir",font=('Times', 12,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.regresa)
        Regresar.pack(side="left")
        
        Viaje = Button(self.VentanaPrin, text="Comenzar viaje",font=('Times', 12,BOLD),bg='#3a7ff6', bd=0,fg="#fff", command=self.comienzoV)       
        Viaje.pack(side="right")
       
        #Creación de marcadores en el mapa
        self.EstacionPrincipal = self.ventana_mapa.set_marker(float(self.origen_latitud), float(self.origen_longitud), text=self.origen)
        self.Parada1 = self.ventana_mapa.set_marker(float(self.estaciones_latitudes[0]), float(self.estaciones_longitudes[0]), text=f"{self.estaciones[0]} \n{ruta.distancias[0]} \n{ruta.tiempos[0]}\n{ruta.horas_llegada[0]}")
        self.Parada2 = self.ventana_mapa.set_marker(float(self.estaciones_latitudes[1]), float(self.estaciones_longitudes[1]), text=f"{self.estaciones[1]} \n{ruta.distancias[1]} \n{ruta.tiempos[1]}\n{ruta.horas_llegada[1]}")
        self.Parada3 = self.ventana_mapa.set_marker(float(self.estaciones_latitudes[2]), float(self.estaciones_longitudes[2]), text=f"{self.estaciones[2]} \n{ruta.distancias[2]} \n{ruta.tiempos[2]}\n{ruta.horas_llegada[2]}")
        self.path()
        
    #Destruye todas las páginas y reinicia de nuevo
    def regresa(self)->None:
        self.VentanaPrin.destroy()
        rutitas()
    
    def comienzoV(self)->None:
        self.VentanaPrin.destroy()
        for i in range(len(self.estaciones)):
            login(f"Iniciar Sesión \n{self.estaciones[i]}","#699e30", False)
            estadisticas(self.horas_llegada,self.distancias[i],self.horas_llegada[i],self.horas_llegada[3], self.estaciones, i)    
            

    #Función que contiene como opciones los datos de latitud y longitud de las paradas
    def opciones(self):
        #camino ruta 1 
        if self.opcion == 1:
            
            self.estaciones.append("Estadio")
            self.estaciones.append("Caribe verde")
            self.estaciones.append("Uni atlantico")
            self.estaciones_latitudes.append("10.923466")
            self.estaciones_latitudes.append("10.956486")
            self.estaciones_latitudes.append("11.020045")
            self.estaciones_longitudes.append("-74.801403")
            self.estaciones_longitudes.append("-74.836018")
            self.estaciones_longitudes.append("-74.871536")
            self.mapaset_latitud= 10.972466
            self.mapaset_longitud= -74.801403
            self.zoom = 13           
                                                                                 
        elif self.opcion == 2:

            self.estaciones.append("Camino murillo")
            self.estaciones.append("Puente murillo")
            self.estaciones.append("Malecon")
            self.estaciones_latitudes.append("10.949140")
            self.estaciones_latitudes.append("10.993557")
            self.estaciones_latitudes.append("11.007782")
            self.estaciones_longitudes.append("-74.799787")
            self.estaciones_longitudes.append("-74.783058")
            self.estaciones_longitudes.append("-74.790303")
            self.mapaset_latitud= 10.962466
            self.mapaset_longitud= -74.801403
            self.zoom = 13
    
    #Función que crea el camino en el mapa
    def path (self):
        if self.opcion == 1:
                   
            camino = self.ventana_mapa.set_path([self.EstacionPrincipal.position, (10.9111870, -74.7990051), (10.9246713, -74.7990072), (10.9226346, -74.7989926),
            (10.9246330, -74.7990301),(10.9247950, -74.7988268), (10.9248388, -74.7986020),(10.9246176, -74.7983204),(10.9241891, -74.7982484),
            (10.9238961, -74.7983396),(10.9235902, -74.7986120),(10.9227221, -74.8152590),(10.9229076, -74.8165056),
            (10.9298006, -74.8311699),(10.9319012, -74.8332558),(10.9342231, -74.8341894),(10.9355293, -74.8343492),(10.9465867, -74.8333519),
            (10.9475199, -74.8334914),(10.9637184, -74.8381301),(10.9651962, -74.8383188),(10.9675345, -74.8382277),(10.9716051, -74.8369754),
            (10.9743193, -74.8363769),(10.9759596, -74.8360294),(10.9810867, -74.8359865),(10.9814404, -74.8360670),(10.9856068, -74.8361206),
            (10.9885513,-74.8365550), (10.9909201, -74.8373608), (11.0027361, -74.8417321), (11.0047619, -74.8419537),(11.0076067, -74.8416892),
            (11.0160255, -74.8384068), (11.0174540, -74.8377987),(11.0163783, -74.8352267),(11.0144491, -74.8360260),(11.0152687,-74.8373242),
            (11.0163171, -74.8398488),(11.0165757, -74.8414179),(11.0165283, -74.8471997),(11.0166073, -74.8473929),(11.0165231, -74.8479508),
            (11.0175145, -74.8519171),(11.0176147, -74.8520820),(11.0175290, -74.8522536),(11.0175554, -74.8530151),(11.0169867, -74.8594012),
            (11.0172308, -74.8599423),(11.0178555, -74.8607799),(11.0188092, -74.8638374),(11.0189250,-74.8640198),(11.0189145, -74.8642236),
            (11.0202414, -74.8714012)
            ])#argumentos a usar deben ser en (latitud, longitud)
            
        elif self.opcion == 2:

            camino = self.ventana_mapa.set_path([self.EstacionPrincipal.position, (10.9111870, -74.7990051), (10.9246713, -74.7990072), (10.9226346, -74.7989926),
            (10.9246330, -74.7990301),(10.9385897, -74.7991562),(10.9425785, -74.7994826), (10.9477525, -74.7997225), self.Parada1.position, 
            (10.9503086, -74.7997660),(10.9509037, -74.7994602),(10.9526050, -74.7975183),(10.9531920, -74.7971365),(10.9593033, -74.7942952),
            (10.9612677, -74.7932545),(10.9617521, -74.7931580),(10.9666514, -74.7909331),(10.9690185, -74.7901163),(10.9872869, -74.7848044),
            (10.9915751, -74.7832448), self.Parada2.position, (10.9961547, -74.7828739),(10.9968182, -74.7826271), (10.9989742, -74.7836785), 
            (11.0003964, -74.7838559),(11.0015861, -74.7843223),(11.0027010, -74.7852465),(11.0052708, -74.7887012),self.Parada3.position,
            (11.0073031, -74.7909946),(11.0071452, -74.7914774),(11.0063948, -74.7905042),(11.0070635, -74.7898551)])
        
        #Muestra la opción para poner un marcador
        def Marcador(coordenada):
            print("Marcador añadido:", coordenada)
            Nuevo_Marcador = self.ventana_mapa.set_marker(coordenada[0], coordenada[1], text="Parada")
        self.ventana_mapa.add_right_click_menu_command(label="Añadir marcador", command=Marcador, pass_coords=True)

        def Mostrar_coordenadas(coordinates_tuple):
            print("Coordenadas del lugar:", coordinates_tuple[0], coordinates_tuple[1])            
        self.ventana_mapa.add_left_click_map_command(Mostrar_coordenadas)
       
        self.VentanaPrin.mainloop()
