lista = []
CantidadPersonas = int(input("Ingrese la cantidad de personas:"))

for i in range(CantidadPersonas):
    altura = float(input(f"Ingrese la altura de la personas {i}:"))
    lista.append(altura)


alturaBaja = 0
alturaPromedio = 0

for i in range(len(lista)):
    if altura < 1.60:
        alturaBaja += 1
    elif altura > 1.60:
        alturaPromedio += 1
    
    
print("---------------------------")
print(f"Las personas ingresadas fueron {CantidadPersonas}")
print(f"Las personas con estatura baja fueron en total {alturaBaja}")
print(f"Las personas con estatura promedio fueron en total {alturaPromedio}")
