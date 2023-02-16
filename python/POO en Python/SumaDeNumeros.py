class SumaNumeros():
    numero1 = int 
    numero2 = int 
    
    def __init__(self) -> None:
        pass
    
    def crearOperacion(self):
        self.numero1 = int (input("Ingrese el primer numero:"))
        self.numero2 = int (input("Ingrese el segundo numero:"))
    
    def Suma(self):
        print("-----------------------------")
        self.suma = self.numero1 + self.numero2
        print (f"La suma de el numero {self.numero1} y el numero {self.numero2} es: {self.suma}")
        print("-----------------------------")
        
    def Resta(self):
        self.resta = self.numero1 - self.numero2
        print(f"La resta del numero {self.numero1} y el numero {self.numero2} es: {self.resta}")
        print("-----------------------------")
        
    def Multiplicacion(self):
        self.multiplicacion = self.numero1 * self.numero2
        if self.numero1 == 0 or self.numero2 == 0:
            print("No se puede multiplicar por 0")
            self.multiplicacion = 0
        print(f"La multiplicacion del numero {self.numero1} y el numero {self.numero2} es: {self.multiplicacion}")
        print("-----------------------------")
        
    def Division(self):
        self.division = self.numero1 / self.numero2
        if self.numero1 == 0 or self.numero2 == 0:
            print("No se puede dividir por 0")
            self.division = 0
        print(f"La division del numero {self.numero1} y el numero {self.numero2} es: {self.division}")
        print("-----------------------------")
        
        
calcular = SumaNumeros()

calcular.crearOperacion()
calcular.Suma()
calcular.Resta()
calcular.Multiplicacion()
calcular.Division()