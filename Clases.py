import requests
import json
import time
import time
class Estacion:
    def __init__(self, nombre: str, ubicacion: str) -> None:
        self.nombre = nombre
        self.tiempo_ideal = 0
        self.next = None
        self.previous = None
        self.ubicacion= ubicacion
  

class Ruta:
    def __init__(self):
        self.PTR = None
        self.last = None
        self.distancias = []
        self.tiempos = []
        self.horas_llegada = []
    
            
    def agregar (self, nombre :str, ubicacion: str)-> None:
        temp = Estacion(nombre, ubicacion)
        if(self.PTR == None):
            self.PTR = temp
            self.last = temp
            
        else:
            self.last.next = temp
            aux = self.last
            self.last = temp
            self.last.previous = aux
    
    def tiempos_ideales(self)->None:
        
        origen = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
        destino = "&destinations="
        nueva_direcion = "%7C"
        API_KEY = "&key=AIzaSyC11D7S2Tiv8IZb-kOpz06-PEEi1-zeYXE"
        modo = "&transit_mode=bus"
       
        url = origen+self.PTR.ubicacion+destino+self.PTR.next.ubicacion+nueva_direcion+self.PTR.next.next.ubicacion+nueva_direcion+nueva_direcion+self.PTR.next.next.next.ubicacion+modo+API_KEY
        respuesta = requests.get(url=url).json()
        self.save_data(respuesta=respuesta)
        
        
        
    def save_data (self, respuesta)-> None:
        for obj in respuesta['rows']:
            for data in obj ['elements']:
                self.distancias.append((data['distance']['text']))
                self.tiempos.append((data['duration']['text']))
    
    
    def sumar_horas(self)->None:
        for times in self.tiempos:    
            hora_salida1 = time.strftime("%H:%M")
            hora_adicional = int(times[0] + times[1])
            hora_salida_min = int(hora_salida1[3]+hora_salida1[4])
            hora_salida_horas = int(hora_salida1[0]+hora_salida1[1])

            if(hora_adicional + hora_salida_min < 60):
                nuevos_min = hora_adicional + hora_salida_min
                hora_salida =  hora_salida1[0]+hora_salida1[1]+":"+ str(nuevos_min // 10) + str(nuevos_min % 10)
            else:
                nuevos_min = (hora_adicional + hora_salida_min) % 60
                horas_sumar = (hora_adicional + hora_salida_min) // 60

                nueva_hora = hora_salida_horas + horas_sumar

                if(nueva_hora < 10):
                    hora_salida =  "0"+str(nueva_hora)+":"+ str(nuevos_min // 10) + str(nuevos_min % 10)
                elif(nueva_hora < 24):
                    hora_salida =  str(nueva_hora // 10) + str(nueva_hora % 10)+":"+ str(nuevos_min // 10) + str(nuevos_min % 10)
                else:
                    hora_salida =  "0" + str(nueva_hora % 24)+":"+ str(nuevos_min // 10) + str(nuevos_min % 10)
            
            hora_salida_horas = int(hora_salida[0]+hora_salida[1])
            if(hora_salida_horas >= 12):
                hora_salida = hora_salida + " pm"
            else:
                hora_salida = hora_salida + " am"
            self.horas_llegada.append(hora_salida)
        self.horas_llegada.append(time.strftime("%H:%M"))
        
    
  

        



