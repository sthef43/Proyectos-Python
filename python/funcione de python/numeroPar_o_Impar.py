def validacion ():
    if num % 2 == 0:
        print(f"El numero ingresado es par")
    else:
        print(f"El numero ingresado es impar")    
    
num = int(input("Ingrese un numero:"))
validacion()