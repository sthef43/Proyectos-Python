class persona:
    nombre = str
    edad = int
    sexo = str
    peso = float
    altura = float  
    confir = bool
    
    def __init__(self,nombre,edad,sexo,peso,altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    
    def crearPersona(self):
        if self.sexo == 'm' or 'M' or 'h' or 'H' or 'o' or 'O':
             print(f"El sexo de la persona creada es {self.sexo}")
        else:
            print("El sexo ingresado no es valido")
            
    def calcularIMC(self):
        if (self.peso/(self.altura**2)) < 20:
            print("La persona ingresada esta por debajo del peso promedio: -1")
        elif (self.peso/(self.altura**2)) > 20 and (self.peso/(self.altura**2)) < 25:
            print("La persona ingresada esta en el eso promedio: 0")
        elif (self.peso/(self.altura**2)) > 25:
            print("La persona ingresada esta sobre el peso promedio: 1")
        
    def esMayor(self):
        if self.edad >= 18:
                self.confir = True
                print(f"La persona es mayor de edad {self.confir}")
        elif self.edad < 18 :
                self.confir = False
                print(f"La persona es mayor de edad {self.confir}")
            

print("---------------PERSONA 1--------------")
Persona1 = persona("Sthefano",1,'H',59,1.69)
Persona1.crearPersona()
Persona1.calcularIMC()
Persona1.esMayor()
print("---------------PERSONA 2--------------")
Persona2 = persona("Santino",19,'H',54,1.70)
Persona2.crearPersona()
Persona2.calcularIMC()
Persona2.esMayor()
print("---------------PERSONA 3--------------")
Persona3 = persona("Ariel",42,'H',105,1.75)
Persona3.crearPersona()
Persona3.calcularIMC()
Persona3.esMayor()
print("---------------PERSONA 4--------------")
Persona4 = persona("Jesica",43,'M',100,1.50)
Persona4.crearPersona()
Persona4.calcularIMC()
Persona4.esMayor()
print("---------------ESTADISTICAS--------------")

todo = Persona1.confir,Persona2.confir,Persona3.confir,Persona4.confir

contadorMayores = 0
contadorMenores = 0

for i in todo:
    if i:
        contadorMayores += 1
    else:
        contadorMenores += 1

print(f"El total de personas menores son: {contadorMenores}")
print(f"El total de personas mayores son: {contadorMayores}")



