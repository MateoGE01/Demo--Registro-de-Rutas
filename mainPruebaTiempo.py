from PruebaTiempo import *


estacion1_latitud = "10.923466"
estacion1_longitud = "-74.801403"
estacion2 = "Caribe verde"
estacion2_latitud = "10.956486"
estacion2_longitud = "-74.836018"
final = "Uni atlantico"
final_latitud = "11.020045"
final_longitud = "-74.871536"
mapaset_latitud= 10.972466
mapaset_longitud= -74.801403
zoom = 13 

ruta = Ruta()
ruta.agregar(self.origen, self.origen_latitud+"%2C"+self.origen_longitud)
ruta.agregar(self.estacion1, self.estacion1_latitud+"%2C"+self.estacion1_longitud)
ruta.agregar(self.estacion2, self.estacion2_latitud+"%2C"+self.estacion2_longitud) 
ruta.agregar(self.final, self.final_latitud+"%2C"+self.final_longitud)
ruta.tiempos_ideales()
ruta.tiempos_ideales()