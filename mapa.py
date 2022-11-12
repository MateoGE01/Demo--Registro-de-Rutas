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





VentanaPrin = Tk()#ventana principal, será cambiada cuando vaya en el código principal

VentanaPrin.geometry("600x400")

VentanaPrin.title("Mapita")

##Mapa en la ventana

ventana_mapa = TkinterMapView(VentanaPrin, width=600, height=400, corner_radius=0)

ventana_mapa.pack(fill="both", expand=True)

ventana_mapa.set_position(10.910700, -74.795472)
ventana_mapa.set_zoom(12)

EstacionPrincipal = ventana_mapa.set_marker(10.910700, -74.795472, text=f"Terminal")

print(EstacionPrincipal.position, EstacionPrincipal.text)#position pasa una ubicacion al formato (latitud, longitud)

Parada1 = ventana_mapa.set_marker(11.0064857, -74.8260246, text=f"Parada 1 \n{Ruta_universidad.tiempos[0]}")

camino1 = ventana_mapa.set_path([EstacionPrincipal.position, (11.0059960, -74.8264058), (11.0066252, -74.8262096) , Parada1.position ])#los argumentos a usar deben ser en (latitud, longitud)

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
