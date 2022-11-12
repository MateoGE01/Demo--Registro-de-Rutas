from Clases import *
from tkinter import *
from tkintermapview import *
from numpy import sin, cos, arccos, pi, round
from geopy.distance import geodesic
from Clases import *








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

ventana_mapa.set_position(mapaset_latitud, mapaset_longitud)
ventana_mapa.set_zoom(zoom=zoom)

EstacionPrincipal = ventana_mapa.set_marker(float(origen_latitud), float(origen_longitud), text=origen)
Parada1 = ventana_mapa.set_marker(float(estacion1_latitud), float(estacion1_longitud), text=f"{estacion1} \n{ruta.distancias[0]} \n{ruta.tiempos[0]}")
Parada2 = ventana_mapa.set_marker(float(estacion2_latitud), float(estacion2_longitud), text=f"{estacion2} \n{ruta.distancias[1]} \n{ruta.tiempos[1]}")
Parada3 = ventana_mapa.set_marker(float(final_latitud), float(final_longitud), text=f"{final} \n{ruta.distancias[2]} \n{ruta.tiempos[2]}")







#camino ruta 1 

camino = ventana_mapa.set_path([EstacionPrincipal.position, (10.9111870, -74.7990051), (10.9246713, -74.7990072), (10.9226346, -74.7989926),
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
  ])#los argumentos a usar deben ser en (latitud, longitud)


#camino ruta 2

"""
camino = ventana_mapa.set_path([EstacionPrincipal.position, (10.9111870, -74.7990051), (10.9246713, -74.7990072), (10.9226346, -74.7989926),
 (10.9246330, -74.7990301),(10.9385897, -74.7991562),(10.9425785, -74.7994826), (10.9477525, -74.7997225), Parada1.position, 
 (10.9503086, -74.7997660),(10.9509037, -74.7994602),(10.9526050, -74.7975183),(10.9531920, -74.7971365),(10.9593033, -74.7942952),
 (10.9612677, -74.7932545),(10.9617521, -74.7931580),(10.9666514, -74.7909331),(10.9690185, -74.7901163),(10.9872869, -74.7848044),
 (10.9915751, -74.7832448), Parada2.position, (10.9961547, -74.7828739),(10.9968182, -74.7826271), (10.9989742, -74.7836785), 
 (11.0003964, -74.7838559),(11.0015861, -74.7843223),(11.0027010, -74.7852465),(11.0052708, -74.7887012),Parada3.position,
 (11.0073031, -74.7909946),(11.0071452, -74.7914774),(11.0063948, -74.7905042),(11.0070635, -74.7898551)
 ])
"""


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
