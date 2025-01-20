from os import system
system("cls")
import time
c=0
h=0
ch=0
ca=0
ra=0
total=0
total2=0
total3=0
while True:
    print("bievenido al merka do")
    print("1.- Comprar")
    print("2.- Pagar")
    print("3.- Salir")
    opc=int(input(">>> "))
    system("cls")
    if opc==1:
        while True:
            print("que desea comprar")
            print("1.- caco cola $1500")
            print("2.- helado $2500")
            print("3.- chocolate $1000")
            print("4.- carne $5500")
            print("5.- ramias $1500")
            print("6.- volver al inicio")
            op=int(input(">>> "))
            
            if op ==1:
                print(" se agrego caco cola $1500")
                total=total+1500
                c=c+1
                input("presione enter")
                system("cls")
            elif op ==2:
                print("se agrego helado $2500")
                total =total+2500
                h=h+1
                input("presione enter")
                system("cls")
            elif op ==3:
                print("se agrego chocolate $1000")
                total=total+1000
                ch=ch+1
                input("presione enter")
                system("cls")
            elif op ==4:
                print("se agrego carne $5500")
                total=total+5500
                ca=ca+1
                input("presione enter")
                system("cls")
            elif op ==5:
                print("se agrego ramias $1500")
                total=total+1500
                ra=ra+1
                input("presione enter")
                system("cls")
            elif op ==6:
                print("volviendo al inicio")
                time.sleep(1)
                input("presione enter")
                break
            else:
                print("opcion invalida")
    elif opc ==2:
        print("esta pasando por caja")
        print(f"su total es de ${total}")
        total2=total*1.19
        print(f"su total con el iva incluido es de {total2}")
        input("presione enter para pagar")
        system("cls")
        while True:
            print("con que desea pagar?")
            print("recuerde que cada metodo de pago tiene una comision")
            print("1.- efectivo + 0%")
            print("2.- debito + 1,5%")
            print("3.- credito + 2,89%")
            opp=int(input(">>> "))
            time.sleep(1)
            system("cls")
            if opp==1:
                print("se secciono efectivo")
                print(f"su total es de {total2}")
                input("presione enter para volve al inicio")
                system("cls")
                break
            elif opp==2:
                print("se secciono debito")
                total2=total2*1.5
                print(f"su total es de {total2}")
                input("presione enter para volve al inicio")
                system("cls")
                break
            elif opp==3:
                print("se secciono credito")
                total2=total2*2.89
                print(f"su total es de {total2}")
                input("presione enter para volve al inicio")
                system("cls")
                break
            else:
                print("opcion invalida\n")
    elif opc==3:
        total3=total2-total
        print("gracias por su visita\n")
        print("------------------------------------")
        print(f"caco cola {c}")
        print(f"helado {h}")
        print(f"chocolate {ch}")
        print(f"carne {ca}")
        print(f"ramias {ra}")
        print("------------------------------------")
        print(f"Subtotal ${total}, IVA ${total3} TOTAL ${total2}\n")
        break
    else:
        print("opcion invalida\n")