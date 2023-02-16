class Circunferencia:
    radio = float
    
    def __init__(self):
        pass
    
    def CrearCircunferencia(self):
        self.radio = float(input("Ingrese el radio de la circunferencia:"))
        
    def Area(self):
        self.area = 3.14 * self.radio
        print(f"El area de la circunferencia es: {self.area}")    
        
    def Perimetro(self):
        self.perimetro = 2 * 3.14 * self.radio
        print(f"El perimetro de la circunferencia es: {self.perimetro}")    
        
        
        
        
        
redondo = Circunferencia()

redondo.CrearCircunferencia()
print("-----------------------------")
redondo.Area()
redondo.Perimetro()