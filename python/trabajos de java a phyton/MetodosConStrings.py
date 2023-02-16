contadorCoreectas = 0
contadorIncorrectas = 0
FDE = str


while FDE != "&&&&&" :
    RS323 = str(input("Ingrese una cadena que empiece con X y O, y deben ser de 5 caracteres maximo:"))
    CaracterdesDe5 = len(RS323)
    primeraLetra = RS323[0]
    ultimaLetra = RS323[4]
    
    if CaracterdesDe5 <= 5 and primeraLetra.__eq__("X") and ultimaLetra.__eq__("O"):
        contadorCoreectas += 1
    else:
        contadorIncorrectas += 1
    
    FDE = str(input("Ingrese el carater especial si desea salir:"))
        
print("Las cadenas ingresadas correctass fueron:", contadorCoreectas)
print("Las cadenas ingresadas incorrectamente fueron:", contadorIncorrectas)