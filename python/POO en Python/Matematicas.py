import random
from math import sqrt

class Matematicas:
    num1 = float
    num2 = float
    
    def __init__(self) -> None:
        pass
    
    def Random(self):
        self.num1 = random.randint(1,100)
        self.num2 = random.randint(1,100)
    
    def retornarMayor(self):
        if self.num1 > self.num2:
            self.mayor = self.num1
            self.menor = self.num2
        elif self.num1 < self.num2:
            self.mayor = self.num2
            self.menor = self.num1
        print(f"El numero mayor es {self.mayor}")
        print(f"El numero menor es {self.menor}")
        
    def calcularPotencia(self):
        self.potenciacion= self.mayor ** self.menor
        
        print(f"La potencia del numero mayor, elevado el numero menor es {self.potenciacion}")
        
    def calcularRaiz(self):
        self.raiz = sqrt(self.menor)
        
        print(f"La raiz cuadrada del numero menor es: {self.raiz}")

mate = Matematicas()
mate.Random()
mate.retornarMayor()
mate.calcularPotencia()
mate.calcularRaiz()

