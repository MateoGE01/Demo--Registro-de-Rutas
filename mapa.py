from Clases import *
from tkinter import *
from tkintermapview import *
from numpy import sin, cos, arccos, pi, round
from geopy.distance import geodesic
from Clases import *

Ruta_universidad = Ruta()

Ruta_universidad.agregar("Terminal", "10.910700%2C-74.795472")
Ruta_universidad.agregar("Estadio", "10.923466%2C-74.801403")
Ruta_universidad.agregar("Caribe verde", "10.956486%2C-74.836018") 
Ruta_universidad.agregar("Uni atlantico", "11.020045%2C-74.871536")
Ruta_universidad.tiempos_ideales()

print(Ruta_universidad.tiempos[0])
print(Ruta_universidad.distancias[0])






#ruta 1

origen = "Terminal"
origen_latitud = "10.910700"
origen_longitud = "-74.795472"
estacion1 = "Estadio"
estacion1_latitud = "10.923466"
estacion1_longitud = "-74.801403"
estacion2 = "caribe verde"
estacion2_latitud = "10.956486"
estacion2_longitud = "-74.836018"
final = "Uni atlantico"
final_latitud = "11.020045"
final_longitud = "-74.871536"


mapaset_latitud= 10.972466
mapaset_longitud= -74.801403
zoom = 13


#ruta 2

"""
origen = "Terminal"
origen_latitud = "10.910700"
origen_longitud = "-74.795472"
estacion1 = "Camino murillo"
estacion1_latitud = "10.949140"
estacion1_longitud = "-74.799787"
estacion2 = "Puente murillo"
estacion2_latitud = "10.993557"
estacion2_longitud = "-74.783058"
final = "Malecon"
final_latitud = "11.007782"
final_longitud = "-74.790303"

mapaset_latitud= 10.962466
mapaset_longitud= -74.801403
zoom = 13
"""

ruta = Ruta()

ruta.agregar(origen, origen_latitud+"%2C"+origen_longitud)
ruta.agregar(estacion1, estacion1_latitud+"%2C"+estacion1_longitud)
ruta.agregar(estacion2, estacion2_latitud+"%2C"+estacion2_longitud) 
ruta.agregar(final, final_latitud+"%2C"+final_longitud)
ruta.tiempos_ideales()





VentanaPrin = Tk()#ventana principal, será cambiada cuando vaya en el código principal

VentanaPrin.geometry("600x400")

VentanaPrin.title("Mapita")

##Mapa en la ventana

ventana_mapa = TkinterMapView(VentanaPrin, width=600, height=400, corner_radius=0)

ventana_mapa.pack(fill="both", expand=True)

EstacionPrincipal = ventana_mapa.set_address("Berlinas de la 93, Barranquilla, Colombia", marker=True)
EstacionPrincipal.set_text("Estación Principal")
print(EstacionPrincipal.position, EstacionPrincipal.text)#position pasa una ubicacion al formato (latitud, longitud)

Parada1 = ventana_mapa.set_marker(11.0064857, -74.8260246, text="Parada 1")


#----------------------------------------------------------------------------#
lugar1= (EstacionPrincipal.position[0],EstacionPrincipal.position[1])
lugar2= (Parada1.position[0],Parada1.position[1])
distancia = (geodesic(lugar1,lugar2).km)
print(distancia, "kilometer")


#-------------------------------------------------------------------------------#

def Marcador(coordenada):
    print("Marcador añadido:", coordenada)
    Nuevo_Marcador = ventana_mapa.set_marker(coordenada[0], coordenada[1], text="Parada")

ventana_mapa.add_right_click_menu_command(label="Añadir marcador", command=Marcador, pass_coords=True)

def Mostrar_coordenadas(coordinates_tuple):

    print("Coordenadas del lugar:", coordinates_tuple[0], coordinates_tuple[1])
    
ventana_mapa.add_left_click_map_command(Mostrar_coordenadas)

VentanaPrin.mainloop()
