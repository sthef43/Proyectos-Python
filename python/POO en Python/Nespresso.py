class Nespresso():
    cantidadActual = float
    
    def __init__(self,capacidadMaxima):
        self.capacidadMaxima = capacidadMaxima
    
    def llenarCafetera(self):
        self.cantidadActual = self.capacidadMaxima
        
    def servirTaza(self):
        self.taza = int(input("Ingrese el tamaño de la taza:"))
        if self.taza > self.cantidadActual:
            self.taza -= self.cantidadActual
            print(f"La taza no alcanzo a llenarse, falto {self.taza} para que se llene")
        else:
            print("La taza se pudo llenar sin problemas")
        
    def vaciarCafetera(self):
        self.op = str(input("Ingrese s si desea vaciar la cafetera, sino desea vaciar ingrese otro caracter"))
        if self.op.__eq__("s"or"S"):
            print("La cafetera se vacio con exito")
            self.cantidadActual = 0
        else:
            print("La cantidad de cafe sigue igual")
    
    def agregarCafe(self):
        self.agregar = int(input("Ingrese la cantidad de cafe que quiere añadir a la cafetera:"))
        self.cantidadActual += self.agregar
        print(f"La cafetera de lleno y quedo en {self.cantidadActual}")
        
    
        
cafe = Nespresso(capacidadMaxima=10)
cafe.llenarCafetera()
cafe.servirTaza()
cafe.vaciarCafetera()
cafe.agregarCafe()