class Mercado:
    
    Producto = {}
    
    def __init__(self) -> None:
        pass
    
    
    def ingresarProducto(self):
        self.productosIngresar = int(input("Ingrese cuantos productos va ah ingresar:"))
        for self.x in range(self.productosIngresar):
            self.nombreProducto = str(input("Ingrese el nombre del producto:"))
            self.precioProducto = (input("Ingrese el precio del producto:"))
            self.d = {self.nombreProducto:self.precioProducto}
            self.Producto.update(self.d)
        
        for self.x in self.Producto.items():
            print(self.x)
        
    def modificarPrecio(self):
        self.ProductoIngresado = str(input("Ingrese un producto para modificar su precio:"))
        for self.key,self.value in self.Producto.items():
            if self.ProductoIngresado in self.Producto:
                self.nuevoPrecio = float(input("Ingrese un nuevo precio para el producto:"))
                self.Producto[self.key] = self.nuevoPrecio
                break
            else:
                print("No se encontro el producto:")
        print(self.Producto)
    
    def eliminarProducto(self):
        self.ProductoIngresado = str(input("Ingrese un producto que quiera eliminar:"))
        for self.key,self.value in self.Producto.items():
            if self.ProductoIngresado in self.Producto:
                self.Producto.pop(self.ProductoIngresado)
                print(self.Producto)
                break
            else:
                print("No se encontro un producto con ese nombre")
    
    def productosIguales(self):
        self.contadorRepetidos = 0
        self.ProductoIngresado = (input("Ingrese un numero para ver que tenemos de ese precio:"))
        for self.x in self.Producto.values():
            if self.ProductoIngresado in self.x:
                self.contadorRepetidos += 1
        
        print(f"la cantidad de productos con el mismo precio es de: {self.contadorRepetidos}")


kiosco = Mercado()

op = 0
while op < 5:
    print("--------------------------")
    print("Ingrese 1 para ingresar productos")
    print("Ingrese 2 para eliminar los productos ya colocados")
    print("Ingrese 3 par saber los productos iguales")
    print("Ingrese 4 para salir")
    print("--------------------------")
    
    op = int(input("Ingres una opcion:"))
    
    match op:
        case 1:
            print("--------------------------")
            kiosco.ingresarProducto()
        case 2:
            print("--------------------------")
            kiosco.eliminarProducto()
        case 3:
            print("--------------------------")
            kiosco.productosIguales()
        case 4:
            print("--------------------------")
            confirmar = str(input("Seguro que desea salir:"))
            if confirmar.__eq__("si"):
                op += 1
                break
            else:
                op -=1
                break
                
    