class CuentaBancaria():
    numeroDeCuenta = int
    Dni = int
    saldoActual = int
    
    def __init__(self) -> None:
        pass
    
    def crearCuenta(self):
        self.numeroDeCuenta = int(input("Ingrese el numero de cuenta:"))
        self.Dni = int = (input("Ingrese su DNI:"))
        self.saldoActual = int(input("Ingrese el saldo actual:"))
        
    def ingresarDinero(self):
        self.ingreso = float(input("Ingrese la cantidad de dinero que quiere agregar:"))
        self.saldoActual = self.saldoActual + self.ingreso
        print(f"El total con el saldo actual mas el ingreso es {self.saldoActual}")
        
    def RetirarDinero(self):
        self.retirar = float(input("Ingrese la cantidad que quiere retirar:"))
        if self.retirar > self.saldoActual:
            self.saldoActual = 0
            print(f"Lo ingresado para retirar es mayor a tu saldo actual, por lo cual la cuenta queda en 0")
        else:
            self.saldoActual -= self.retirar        
            print(f"tu sueldo es mayor a la cantidad de retiro, por lo cual tu saldo actual queda en {self.saldoActual}")
    
    def extraccionRapida(self):
        self.extraer = float(input("Ingrese el porcentaje de extraccion, solo se puede el 20%:"))
        if (self.extraer <= 20):
            self.Solo20 = self.saldoActual * (self.extraer / 100)
            self.saldoCon20 = self.saldoActual - self.Solo20
            print(f"Ingreso el 20% por lo cual lo que podra extraer es {self.Solo20}")
        else:
            print("Ingreso mas del 20%, por lo cual la operacion se cancela")
            
    def consultarSaldo(self):
        self.op = str(input("Ingrese s, si desea consultar su saldo, de lo contrario ingrese otra letra:"))
        if self.op.__eq__("s"):
            print(f"El saldo acutal de su cuenta es {self.saldoActual}")
        else:
            print("Ingreso un caracter equivocado")
    
    def consultarDatos(self):
        self.op = str(input("Ingrese s, si desea consultar sus datos, de lo contrario ingrese otro caracter"))
        if self.op.__eq__("s"):
            print(f"El DNI del cliente es {self.Dni} y su numero de cuenta es {self.numeroDeCuenta}")               
        

crear = CuentaBancaria()

crear.crearCuenta()
crear.ingresarDinero()
crear.RetirarDinero()
crear.extraccionRapida()
crear.consultarSaldo()
crear.consultarDatos()