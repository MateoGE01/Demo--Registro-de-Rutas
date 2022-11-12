import csv

class placaclave:
    def __init__(self):
        self.login()

    def login(self):
        self.placa = input("Ingrese la placa: ")
        self.clave = input("Ingrese la clave: ")
        with open("PlacasClaves.csv", mode="r") as f:
            reader = csv.reader(f, delimiter = ";")
            for row in reader:
                if row == [self.placa, self.clave]:
                    print("Se ha registrado con exito.")
                    return True
        print("Intentelo de nuevo")
        return False
    

siu = placaclave()




        
