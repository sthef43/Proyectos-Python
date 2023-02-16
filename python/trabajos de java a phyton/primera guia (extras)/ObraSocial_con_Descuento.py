ValorTratamiento = int(input("Ingrese el valor del tratamiento:"))

TipoDeSocio = str(input("Ingrese su tipo de socio, A o B o C:"))

match TipoDeSocio:
    case "A":
        porcentaje_50 = 50
        descuento = ValorTratamiento * (porcentaje_50 / 100)
        valorConDescuento = ValorTratamiento - descuento
        print(f"El valor con un descuento del 50% es: {valorConDescuento}")
    case "B":
        porcentaje_35 = 35
        descuento = ValorTratamiento * (porcentaje_35 / 100)
        valorConDescuento = ValorTratamiento - descuento
        print(f"El valor con un descuento del 35% es: {valorConDescuento}")
    case "C":
        print(f"No reciben un descuento por que no pagan nada, por lo cual pagan el total que es de: {ValorTratamiento}")
        