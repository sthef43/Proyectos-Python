class Paises:
    
    paises = list()
    
    def __init__ (self):
        pass
    
    def agregarPaises(self):
        self.respuestaCorrecta = "si"
        
        while True:
            self.paises.append(input("Ingrese un pais:"))
            
            self.respuesta = str(input("Desea seguir ingresando paises?"))
            if self.respuesta == self.respuestaCorrecta:
                continue
            else:
                break

        print("---------------------------------")
        print(f"el conjunto de paises ingresados es: {self.paises}")
        
    def ordenarPaises(self):
        
        print("---------------------------------")
        self.Listaordenada = list(self.paises)
        self.Listaordenada.sort()
        print(f"El conjunto de paises ordenados es: {self.Listaordenada}")
        
    def eliminarPais(self):
        self.paisSelecionado = str(input("Ingrese un pais de el conjunto que desee eliminar:"))
        for self.x in self.paises:
            if self.paisSelecionado in self.paises:
                self.paises.pop()
                print(f"La lista actualizada quedo como: {self.paises}")
                break
            else:
                print("No se encontro el pais selecionado")

CrearLista = Paises()
CrearLista.agregarPaises()
CrearLista.ordenarPaises()
CrearLista.eliminarPais()