from tkinter import *
from redimension import *
from tkinter import *
from tkintermapview import *
from Clases import *

class mapa:  
                                      
    def __init__(self, opcion): 
        #Creación de variables
        self.opcion = opcion      
        self.origen = "Terminal"
        self.origen_latitud = "10.910700"
        self.origen_longitud = "-74.795472"
        self.estacion1 = None
        self.estacion1_latitud = None
        self.estacion1_longitud = None
        self.estacion2 = None 
        self.estacion2_latitud = None
        self.estacion2_longitud = None
        self.final = None
        self.final_latitud = None
        self.final_longitud = None
        self.mapaset_latitud= None
        self.mapaset_longitud= None
        self.zoom = None    
                  
        self.opciones()
        
        ruta = Ruta()
        ruta.agregar(self.origen, self.origen_latitud+"%2C"+self.origen_longitud)
        ruta.agregar(self.estacion1, self.estacion1_latitud+"%2C"+self.estacion1_longitud)
        ruta.agregar(self.estacion2, self.estacion2_latitud+"%2C"+self.estacion2_longitud) 
        ruta.agregar(self.final, self.final_latitud+"%2C"+self.final_longitud)
        ruta.tiempos_ideales()

        #Creación de la ventana
        self.VentanaPrin = Tk()
        self.VentanaPrin.geometry("1200x700")
        self.VentanaPrin.title("Mapita")

        #Creación del frame y el mapa contenido en la misma
        self.ventana_mapa = TkinterMapView(self.VentanaPrin, width=600, height=400, corner_radius=0)
        self.ventana_mapa.pack(fill="both", expand=True)
        self.ventana_mapa.set_position(self.mapaset_latitud, self.mapaset_longitud)
        self.ventana_mapa.set_zoom(zoom=self.zoom)

        #Creación de marcadores en el mapa
        self.EstacionPrincipal = self.ventana_mapa.set_marker(float(self.origen_latitud), float(self.origen_longitud), text=self.origen)
        self.Parada1 = self.ventana_mapa.set_marker(float(self.estacion1_latitud), float(self.estacion1_longitud), text=f"{self.estacion1} \n{ruta.distancias[0]} \n{ruta.tiempos[0]}")
        self.Parada2 = self.ventana_mapa.set_marker(float(self.estacion2_latitud), float(self.estacion2_longitud), text=f"{self.estacion2} \n{ruta.distancias[1]} \n{ruta.tiempos[1]}")
        self.Parada3 = self.ventana_mapa.set_marker(float(self.final_latitud), float(self.final_longitud), text=f"{self.final} \n{ruta.distancias[2]} \n{ruta.tiempos[2]}")
        self.path()
        




    #Función que contiene como opciones los datos de latitud y longitud de las paradas
    def opciones(self):
        #camino ruta 1 
        if self.opcion == "1":
            
            self.estacion1 = "Estadio"
            self.estacion1_latitud = "10.923466"
            self.estacion1_longitud = "-74.801403"
            self.estacion2 = "Caribe verde"
            self.estacion2_latitud = "10.956486"
            self.estacion2_longitud = "-74.836018"
            self.final = "Uni atlantico"
            self.final_latitud = "11.020045"
            self.final_longitud = "-74.871536"
            self.mapaset_latitud= 10.972466
            self.mapaset_longitud= -74.801403
            self.zoom = 13           
                                                                                 
        elif self.opcion == "2":
            
            self.estacion1 = "Camino murillo"
            self.estacion1_latitud = "10.949140"
            self.estacion1_longitud = "-74.799787"
            self.estacion2 = "Puente murillo"
            self.estacion2_latitud = "10.993557"
            self.estacion2_longitud = "-74.783058"
            self.final = "Malecon"
            self.final_latitud = "11.007782"
            self.final_longitud = "-74.790303"
            self.mapaset_latitud= 10.962466
            self.mapaset_longitud= -74.801403
            self.zoom = 13
    
    #Función que crea el camino en el mapa
    def path (self):
        if self.opcion == "1":
                   
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
            
        elif self.opcion == "2":

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

