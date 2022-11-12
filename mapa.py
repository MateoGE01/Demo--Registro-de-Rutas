from tkinter import *
from tkintermapview import *
from numpy import sin, cos, arccos, pi, round
from geopy.distance import geodesic

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



"""
def left_click_event(coordinates_tuple):
    print("Coordenadas del lugar:", coordinates_tuple[0], coordinates_tuple[1])
    
ventana_mapa.add_left_click_map_command(left_click_event)

"""

"""
# MIDE LA DISTANCIA ENTRE 2 PUNTOS

def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees

def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians

def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2):
    
    theta = longitude1 - longitude2
    
    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) + 
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )
    return round(distance * 1.609344, 2)

#--------------------------------------------------------------

Distancia = getDistanceBetweenPointsNew(EstacionPrincipal.position[0], EstacionPrincipal.position[1], Parada1.position[0], Parada1.position[1])
print(f"{Distancia} km")
"""