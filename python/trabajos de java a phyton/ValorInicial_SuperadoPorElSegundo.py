numeroInicial = int(input("Ingrese un numero inicial:"))
numeroSecunadario = 0
numeroTerciario = 0

while numeroInicial >= numeroTerciario:
    numeroSecunadario = int(input("Ingrese un numero hasta superar el inicial:"))
    numeroTerciario = int(numeroTerciario + numeroSecunadario)
    print("Debes seguir sumando")

print("Pudo superar el valor incial que era", numeroInicial)
print("Ya que", numeroTerciario, "es mayor")