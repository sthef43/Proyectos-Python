class alumnos():
    nombre = []
    notas = []
    totalNotas = []
    
    
    def __init__(self) -> None:
        pass
    
    def crearAlumno(self):
        
        self.cantidadAlumnos = int(input("Ingrese la cantidad de alumnos a ingresar:"))
        print("-----------------------------------------")

        for self.x in range(self.cantidadAlumnos):
            self.nombreAlumno = input("Ingrese el nombre del alumno:")
            self.nombre.append(self.nombreAlumno)
            self.not1 = int(input("Ingrese la nota numero 1:"))
            self.not2 = int(input("Ingrese la nota numero 2:"))
            self.not3 = int(input("Ingrese la nota numero 3:"))
            self.notas.append([self.not1,self.not2,self.not3])
            print("-----------------------------------------")

        for self.x in range(self.cantidadAlumnos):
            self.total = self.notas[self.x][0]+self.notas[self.x][1]+self.notas[self.x][2]
            self.totalNotas.append(self.total)
        print("-----------------------------------------")
        
        for self.x in range(self.cantidadAlumnos):
            print(f"El alumno {self.nombre[self.x]} tiene como notas: {self.notas[self.x][0]},{self.notas[self.x][1]},{self.notas[self.x][2]}")
        
        print(f"El total de las notas es {self.totalNotas}")
        
    def notaFinal(self):
        print("-----------------------------------------")
        self.divisor = 3
        self.alumnoSeleccionado = input("Ingrese el nombre del alumno que desea buscar:")
        for self.i in self.nombre:
            if self.alumnoSeleccionado in self.nombre:
                self.totalNotas = list(map(lambda x: x / self.divisor, self.totalNotas))
                print(f"El promedio final de la alumno {self.alumnoSeleccionado } es: {self.totalNotas}")
                break
            
            
creacion = alumnos()
creacion.crearAlumno()
creacion.notaFinal()