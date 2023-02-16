Cuadrado = int(input("ingrese el tamaño del cuadrado:"))

for fila in range(Cuadrado):
    for columna in range(Cuadrado):
        if fila == 0 or fila == Cuadrado - 1 or columna == 0 or columna == Cuadrado - 1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()