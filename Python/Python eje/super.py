from os import system
system("cls")

total = 0
print("Binvenido a supermerk2")
while True:
    print("1.- Moster $2.500")
    print("2.- Helado $2.000")
    print("3.- Maruchan $1.000")
    print("4.- Te $2.200")
    print("5.- Pagar")
    print("6.- Salir\n")
    opc = int(input(">>> "))
    if opc ==1:
        total = total+2500
        print("Se agrego  Moster $2.500\n")
    elif opc ==2:
        total = total+2000
        print("Se agrego Helado $2.000\n")
    elif opc ==3:
        total = total+1000
        print("Se agrego Maruchan $1.000\n")
    elif opc == 4:
        total = total+2200
        print("Se agrego  Te $2.200\n")
    elif opc == 5:
        print(f"su total a para es ${total}\n")
        while True:
            print("Que metodo de pago desea ?")
            print("1.- Devito %20")
            print("2.- Credito %10")
            print("3.- Efectivo")
            print("4.- Volver a atras")
            op = int(input(">>> "))
            if op ==1:
                total = total*0.80
                print("Su pago se realizo con exito")
                print(f"con el 20% de descuento su total fue de ${total}")
                print("gracias por comprar en supermerk2")
                print("Volviendo al menu\n")
                break
            elif op ==2:
                total = total*0.90
                print("Su pago se realizo con exito")
                print(f"con el 10% de descuento su total fue de ${total}")
                print("gracias por comprar en supermerk2")
                print("Volviendo al menu\n")
                break
            elif op == 3:
                print("Su pago se realizo con exito")
                print(f"Su total fue de ${total}")
                print("Gracias por comprar en supermerk2")
                print("Volviendo al menu\n")
                break
            elif op ==4:
                print("Regresando\n")
                break
            else:
                print("Opcion no valida\n")
    elif opc == 6:
        print("Saliendo, gracias por comprar en supermerk2")
        break
    else:
        print("Opcion no valida\n")

# crea un menu con 4 opcinoes de menu, un apartado para pagar y otro para salir del programa
# cuando se pegue que se muestren 4 opccines devito20% , credito10%,efectivo y volvel atras
# despues de seleccionar la opcion que se aplique el descuentp devido y que salga al menu principal
