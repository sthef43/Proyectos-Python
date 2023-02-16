class Rectangulo():
    base = int
    altura = int
    
    def __init__(self) -> None:
        pass
    
    def CrearRectangulo(self):
        self.base = int(input("Ingrese la base del rectnagulo:"))
        self.altura = int(input("Ingrese la altura del rectangulo:"))
        
    def CalcularSuperficie(self):
        self.superficie = self.base * self.altura
        print(f"La superficie del rectangulo es: {self.superficie}")
    
    def CalcularPerimetro(self):
        self.perimetro = (self.base + self.altura) * 2
        print(f"El perimetro del rectangulo es: {self.perimetro}")
        
    def CrearConAsteriscos(self):
        for i in range(self.base):
            print("* ", end = "")
        print()
        
        for i in range(self.altura - 2):
            print("* ", end="")
            for j in range(self.base - 2):
                print("  ", end="")
            print("*")
        for i in range(self.base):
            print("* ", end="")
    
crear = Rectangulo()


crear.CrearRectangulo()
crear.CalcularSuperficie()
crear.CalcularPerimetro()
crear.CrearConAsteriscos()