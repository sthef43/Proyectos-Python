class Pelicula:
    pelicula = []
    titulo = []
    director = []
    duracion = []


    def __init__(self) -> None:
        pass
    
    def CrearPelicula(self):
        self.totalPeliculas = int(input("Ingrese el total de peliculas que va a ingresar:"))
        
        print("--------------------------------------")
        for self.x in range(self.totalPeliculas):
            print("--------------------------------------")
            self.nombreTitulo = str(input("Ingrese el titulo de la pelicula:"))
            self.titulo.append(self.nombreTitulo)
            self.nombreDirector = str(input("Ingrese el nombre del director:"))
            self.director.append(self.nombreDirector)
            self.cantidadDuracion = int(input("Ingrese la duracion de la pelicula:"))
            self.duracion.append(self.cantidadDuracion)
            self.pelicula.append([self.titulo,self.director,self.duracion])
        print("--------------------------------------")
    
    def mostrarPelicula(self):
        for self.x in range(self.totalPeliculas):
            print(f"el titulo de la pelicula es {self.titulo[self.x]} su director es {self.director[self.x]} y su duracion es de {self.duracion[self.x]}")
          
    def PeliculaMayora1(self):
        self.duracionMayor = 1
        self.mayor = []
        for self.x in self.duracion:
            if self.duracionMayor > 1:
                    print(f"El titulo {self.titulo[self.x]} tiene una duracion mayor a 1 hora")
                
                
                
        
        
cine = Pelicula()
cine.CrearPelicula()
cine.mostrarPelicula()
cine.PeliculaMayora1()