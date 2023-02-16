import re

class Palabra:
    frase = str
    longitud = int
    
    def __init__(self):
        pass
    
    def ingresoPalabra(self):
        print("----------------------------------")
        self.frase = str(input("Ingrese la frase o palabra:"))
        self.longitud = len(self.frase)
        print(f"La frase ingresada es {self.frase} y tiene en total {self.longitud} de palabras")
        print("----------------------------------")
    
    def mostrarVocales(self):
        self.contadorVocales = 0
        
        self.frase.lower
        self.frase.upper
    
        for i in self.frase:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                self.contadorVocales += 1
        
        print(f"La cantidad de vocales que tiene esta frase es de {self.contadorVocales}")
        print("----------------------------------")
    
    def invertirFrase(self):
        pat = re.compile("\w+")
        def invert(m):
            return m.group(0)[::-1]
        
        self.resultado = pat.sub(invert, self.frase)
        print(f"La frase de forma invertida es: {self.resultado}")
        print("----------------------------------")
        
    def vecesRepetido(self):
        self.palabra = (input("Ingrese una letra para buscarla repetida en la frase:"))
        self.longitudPalabra = len(self.palabra)
        self.repetidas = 0
        if self.longitudPalabra <= 1:
            for i in self.frase:
                self.palabras = i.split(' ')
                for p in self.palabras:
                    if p == self.palabra:
                        self.repetidas += 1
        else:
            print("Ingreso mas de una palabra")
            
        print(f"La letra ingresada se repite {self.repetidas}")
        print("----------------------------------")
        
    def compararLongitud(self):
        self.nuevaFrase = str(input("Ingrese una nueva frase:"))
        self.nuevaLongitud = len(self.nuevaFrase)
        if self.nuevaLongitud < self.longitud:
            print(f"La frase {self.nuevaFrase} es menor a {self.frase}")
        else:
            print(f"La frase {self.nuevaFrase} es mayor a {self.frase}")
        print("----------------------------------")
    
    def uniFrases(self):
        self.union = str(input("Ingrese una frase para concatenar con la que ingreso primero:"))
        print(f"El resultado de la concatenacion es {self.frase} {self.union}")
        print("----------------------------------")
        
    def remplazar(self):
        self.remplaza = str(input("Ingrese la palabra por la cual cambiaran todas las letras a:"))
        self.longitudRemplaza = len(self.remplaza)
        if self.longitudRemplaza <= 1:
            self.remplazando = self.frase.replace("a",self.remplaza)
        else:
            print("Ingreso mas de una palabra")
            
        print(f"La frase con la letra a remplazada quedaria como {self.remplazando}")
        print("----------------------------------")
    
    def contiene(self):
        self.palabra_a_verificar = str(input("Ingrese una palabra para verificar que este en la frase:"))
        self.verificador = bool
        
        for i in self.frase:
            self.Palabras = i.split(' ')
            for p in self.Palabras:
                if p == self.palabra_a_verificar:
                    self.verificador = True
                else:
                    self.verificador = False
        
        print(f"La palabra ingresada esta en la frase? {self.verificador}")
                
                 
palabra = Palabra()
palabra.ingresoPalabra()
palabra.mostrarVocales()
palabra.invertirFrase()
palabra.vecesRepetido()
palabra.compararLongitud()
palabra.uniFrases()
palabra.remplazar()
palabra.contiene()