import time
import requests
import json
import time

class Estacion:
    def __init__(self, nombre, ubicacion: str) -> None:
        self.nombre = nombre
        self.tiempo_ideal = 0
        self.next = None
        self.previous = None
        self.ubicacion= ubicacion
    

class Ruta:
    def __init__(self):
        self.hora_partida = None
        self.PTR = None
        self.last = None
        self.size = 0
        self.distancias = []
        self.tiempos = []
        self.horas = []
        
        
    def correr(self):
        actual = self.PTR
        while(actual != None):
            print(f" {actual} ->")
            actual = actual.next
            
    def agregar (self, nombre, ubicacion: str)-> None:
        temp = Estacion(nombre, ubicacion)
        if(self.PTR == None):
            self.PTR = temp
            self.last = temp
            
        else:
            self.last.next = temp
            aux = self.last
            self.last = temp
            self.last.previous = aux

        self.size += 1
    
    def tiempos_ideales(self)->None:
        
        hora_partida = time.strftime("%H:%M")
        self.hora_partida = float(hora_partida[0]+hora_partida[1]+hora_partida[3]+hora_partida[4])


        origen = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
        destino = "&destinations="
        nueva_direcion = "%7C"
        API_KEY = "&key=AIzaSyC11D7S2Tiv8IZb-kOpz06-PEEi1-zeYXE"
        modo = "&transit_mode=bus"
       
        url = origen+self.PTR.ubicacion+destino+self.PTR.next.ubicacion+nueva_direcion+self.PTR.next.next.ubicacion+nueva_direcion+nueva_direcion+self.PTR.next.next.next.ubicacion+modo+API_KEY
        respuesta = requests.get(url=url).json()
        self.save_data(self.distancias,self.tiempos,respuesta)
        
        
        
    def save_data (self,distancias, tiempos, respuesta)-> None:
        for obj in respuesta['rows']:
            for data in obj ['elements']:
                distancias.append((data['distance']['text']))
                tiempos.append((data['duration']['text']))
    
    
        


class bus:
    def _init_(self, codigo) -> None:
        self.codigo = codigo
        
    
    def calcular_horas (self, hora_de_salida, ruta : Ruta):
        actual = ruta.PTR
        horas_ideales = []
         
        while(actual != None):
            horas_ideales.append(self.sumar_horas(int(hora_de_salida), int(actual.tiempo_ideal)))
            actual = actual.next
        for i in horas_ideales:
            print(i)
        
    def sumar_horas(self, hora_de_salida: int, tiempo_sumar : int) -> int:
        if(tiempo_sumar < 60):
            return (hora_de_salida + tiempo_sumar)
        else:
            min = tiempo_sumar % 60
            num_horas = tiempo_sumar // 60
            horas = num_horas * 100

            return (hora_de_salida + horas + min)

