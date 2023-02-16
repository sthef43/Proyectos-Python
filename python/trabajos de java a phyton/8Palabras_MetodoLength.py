palabra = str(input("Ingrese una palabra:"))

longitud_de_8 = len(palabra)

if longitud_de_8 > 8:
    print("La palabra", palabra, "es mayor a 8 palabras")
else:
    print("La palabra", palabra, "es correcta")