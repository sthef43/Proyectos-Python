class libro:
    Isbn = int
    autor = str
    numeroDePaginas = int
    titulo = str
    
    def __init__(self):
        pass
    
    def CrearLibro(self):
        self.Isbn = input("Ingrese el ISBN del libro:")
        self.autor = input("Ingrese el autor del libro:")
        self.numeroDePaginas = input("Ingrese el numero de paginas del libro")
        self.titulo = input("Ingrese el titulo del libro:")
        print(f"El ISBN del libro es: {self.Isbn} su autor es: {self.autor} el numero de paginas en total es de: {self.numeroDePaginas} y su titulo es: {self.titulo}")
        
book = libro()
book.CrearLibro()