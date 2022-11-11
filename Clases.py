class Estacion:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.tiempo_ideal = 0
        self.next = None
        self.previous = None
    def __repr__(self) -> str:
        return str((self.tiempo_ideal))

class Ruta:
    def __init__(self):
        self.PTR = None
        self.last = None
        self.size = 0
    
    def agregar_estaciones (self, N_estaciones : int):
        iterador = 0
        while(iterador < N_estaciones):
            Nombre = str(input("Por favor digite el nombre de la estación: "))
            self.agregar(nombre= Nombre)
            iterador += 1
    
    def correr(self):
        actual = self.PTR
        while(actual != None):
            print(f" {actual} ->")
            actual = actual.next
            
    def agregar (self, nombre)-> None:
        temp = Estacion(nombre)
        if(self.PTR == None):
            self.PTR = temp
            self.last = temp
            
        else:
            self.last.next = temp
            aux = self.last
            self.last = temp
            self.last.previous = aux

            self.last.tiempo_ideal = 20 + self.last.previous.tiempo_ideal 

        self.size += 1

    def __repr__(self) -> str:
        cadena = ""
        actual = self.PTR
        while(actual.next != None):
            cadena += "[" + str(actual.nombre) + "]" + "->"  
            actual = actual.next
        cadena += "[" + str(actual.nombre) + "]"  
      
        return(cadena)
    


class bus:
    def __init__(self, ruta, codigo) -> None:
        self.codigo = codigo
        self.ruta = ruta
        self.horas_ideales = []
    
    def calcular_horas (self, hora_de_salida):
        actual = self.ruta.PTR
        iterador = 0
        while(actual != None):
            self.horas_ideales [iterador] = self.sumar_horas(hora_de_salida, actual.tiempo_ideal)
            iterador += 1
            actual = actual.next
        iterador = 0

        while(actual != None):
            print(self.horas_ideales [iterador])
            iterador += 1
            actual = actual.next
        
            

    def sumar_horas(self, hora_de_salida: int, tiempo_sumar : int) -> int:
        if(tiempo_sumar < 60):
            return (hora_de_salida + tiempo_sumar)
        else:
            min = tiempo_sumar % 60
            num_horas = tiempo_sumar // 60
            horas = num_horas * 100

            return (hora_de_salida + horas + min)