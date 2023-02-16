class Electrodomestico():
    precio = 0
    color = str
    consumo = str
    peso = 0
    
    def __init__(self) -> None:
        pass
    
    def ComprobarConsumoEnergetico(self):
        if self.consumo == 'a' or self.consumo == 'b' or self.consumo == 'c' or self.consumo == 'd' or self.consumo == 'e' or self.consumo == 'f':
            print(f"el consumos que tiene ese de: {self.consumo}")
        else:
            self.consumo = 'f'
            print(f"el consumo que ingreso no esta disponible por lo cual queda en: {self.consumo}")
    
    
    def ComprobarColor(self):
        if self.color == "blanco" or self.color == "negro" or self.color == "rojo" or self.color == "azul" or self.color == "gris":
            print(f"el color que elijio es: {self.color}")
        else:
            self.color = "blanco"
            print(f"el color ingresado no esta disponible por lo cual queda en: {self.color}")
    
    def crearElectrodomestico(self):
        print("---------------------------")
        self.color = str(input("Ingrese el color del electrodomestico:"))
        self.ComprobarColor()
        print("")
        self.consumo = str(input("Ingrese la letra de consumo:"))
        self.ComprobarConsumoEnergetico()
        self.precio=1000
        print("")
        self.peso = int(input("Ingrese el peso del electrodomestico:"))
        print(f"El precio base del electrodomestico es de {self.precio}")
        print("")

    def precioFinal1(self):
        if self.consumo == 'a':
            self.precio += 1000
        elif self.consumo == 'b':
            self.precio += 800
        elif self.consumo == 'c':
            self.precio += 600
        elif self.consumo == 'd':
            self.precio += 500
        elif self.consumo == 'e':
            self.precio += 300
        elif self.consumo == 'f':
            self.precio += 100
            
        if self.peso >= 1 and self.peso <= 19:
            self.precio += 100
        elif self.peso >= 20 and self.peso <= 49:
            self.precio += 500
        elif self.peso >= 50 and self.peso <= 79:
            self.precio += 800
        elif self.peso > 80:
            self.precio += 1000

class Lavadora(Electrodomestico):
    carga = 0
    
    def __init__(self) -> None:
        pass
    
    def crearLavadora(self):
        self.crearElectrodomestico()
        self.carga = int(input("Ingrese la carga que desea en la lavadora:"))
        print("---------------------------")
    
    def precioFinal(self):
        if self.carga > 30:
            self.precio += 500
        elif self.carga <= 30:
            self.carga += 0
        self.precioFinal1()
        print(f"El precio final de este electroomestico es de : {self.precio}")


class Televisor(Electrodomestico):
    resolucion = 0
    sintonizadorTDT = bool
    
    def __init__(self) -> None:
        pass

    def crearTelevisor(self):
        self.crearElectrodomestico()
        self.resolucion = int(input("Ingrese en pulgadas la resolucion del televisor:"))
        self.tieneSintonizador = input("Ingrese si, si tiene sintoizador TDT, de lo contrario ingrese no:")
    
    def precioFinal(self):
        if self.resolucion > 40:
            self.aumento = self.precio * (30/100)
            self.valorTotal = self.precio  + self.aumento
            self.precio = self.valorTotal
        if self.tieneSintonizador.__eq__("si"):
            self.sintonizadorTDT = True
            self.precio += 500
        elif self.tieneSintonizador.__eq__("no"):
            self.sintonizadorTDT = False
            self.precio += 0
        self.precioFinal1()
        print(f"El precio final de este electroomestico es de : {self.precio}")
lavadora = Lavadora()
lavadora.crearLavadora()
lavadora.precioFinal()
print("----------------------")
tele = Televisor()
tele.crearTelevisor()
tele.precioFinal()
