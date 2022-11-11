from Clases import *

Ruta_universidad = Ruta()


#Ruta_universidad.agregar_estaciones(3)


Ruta_universidad.agregar("Murillo soledad")
Ruta_universidad.agregar("Estadio")
Ruta_universidad.agregar("Caribe verde") 
Ruta_universidad.agregar("puente la 38")
Ruta_universidad.agregar("Alamedade del rio")
Ruta_universidad.agregar("miramar")
Ruta_universidad.agregar("corredor universitaro")

bus1 = bus(Ruta_universidad, 1234)
bus1.calcular_horas(1200)
