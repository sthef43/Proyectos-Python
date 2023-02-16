class Animal():
    def __init__(self,nombre,alimento,raza,edad) -> None:
        self.nombre=nombre
        self.alimento=alimento
        self.raza=raza
        self.edad=edad
        
    def estado(self):
        print("Nombre: ", self.nombre, "\nalimento: ", self.alimento, "\nraza: ", self.raza, "\nedad: ", self.edad)
        
    def alimentacion(self):
        print(f"El animal {self.nombre} se alimenta de: {self.alimento}")
    
    
class CrearAnimal(Animal):
    pass

Perro1 = CrearAnimal("hachi","carne","dogo",21)
Perro1.alimentacion()

Perro2 = CrearAnimal("orlando","carne","dogo",21)
Perro2.alimentacion()

Gato = CrearAnimal("wilson","pescado","pelado",4)
Gato.alimentacion()

Pato = CrearAnimal("delfina","bichos","pata",2)
Pato.alimentacion()