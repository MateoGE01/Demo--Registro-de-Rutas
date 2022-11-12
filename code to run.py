from Clases import *





Ruta_universidad = Ruta()

Ruta_universidad.agregar("Terminal", "10.910700%2C-74.795472")
Ruta_universidad.agregar("Estadio", "10.923466%2C-74.801403")
Ruta_universidad.agregar("Caribe verde", "10.956486%2C-74.836018") 
Ruta_universidad.agregar("Uni atlantico", "11.020045%2C-74.871536")
Ruta_universidad.tiempos_ideales()

print(Ruta_universidad.tiempos[0])
print(Ruta_universidad.distancias[0])

