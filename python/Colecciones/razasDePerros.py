raza = []
respuesta = "si"


while respuesta.__eq__("si"):
    razaIngresada = input("Ingrese la raza del perro:")
    raza.append(razaIngresada)
    respuesta = input("Desea seguir?:")
print("-----------------------------")

perroSelecionado = input("Ingrese el nombre de la raza ah eliminar:")
for i in raza:
    if perroSelecionado in raza:
        raza.remove(perroSelecionado)
        raza.sort()
        print("El elemnto ingresado fue eliminado")
        break
    else:
        print("No se encontro ningun elemento con ese nombre")
        break

print(raza)