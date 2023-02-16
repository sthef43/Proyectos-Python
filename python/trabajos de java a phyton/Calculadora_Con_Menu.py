num1 = float(input("Ingrese el primer numero:"))
num2 = float(input("Ingrese el segundo numero:"))
op = 0


while op < 5:
    print("MENU")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
    
    op = int(input("Ingrese una opcion:"))
        
    match op:
        case 1:
            suma = num1 + num2
            print("Elijio la opcion suma:", suma)
            print("----------------------------------")
            continue
        case 2:
            resta = num1 - num2
            print("Elijio la opcion resta:", resta)
            print("----------------------------------")
            continue
        case 3:
            multiplicacion = num1 * num2
            print("Elijio la opcion multiplicacion:", multiplicacion)
            print("----------------------------------")
            continue
        case 4:
            divison = num1 / num2
            print("Elijio la opcion dividir:", divison)
            print("----------------------------------")
            continue
            
        case 5:
            confirmar = str(input("Ingrese s si desea salir, de lo contrario aprete cualquier otra letra:"))
            if confirmar.__eq__("s"):
                op += 1
                break
            else:
                op -= 2
                print("----------------------------------")
                continue