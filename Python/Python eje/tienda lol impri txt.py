from os import system
system("cls")

ite=["Firmamento desgarrado","Coleccionista","Fuerza trinidad","Verdugo de krakens","Eclipse","Rencor de serylda","Tormento de liandry","Robaalmas de Mejai"]
pre=[3100,3000,3333,3100,2900,3000,3000,1500]
champ=["Kayn","Ekko","Viego","Shaco","Warwick","Jhin","Mordekaiser","Lee sin","Irelia","Akali","Leona"]
car=[]
to=0
c=1

print("Bienvenido a la grieta del fornicador")
while True:
    print("1.- Elije tu campeon")
    print("2.- Tienda de objetos")
    print("3.- Pagar y salir")
    op=int(input(">>> "))
    system("cls")
    
    if op ==1:
        print("Elije a tu campeon invocador")
        for ch in champ:
            print(f"{c}.- {ch}")
            c=c+1
        opc=int(input(">>> "))
        opc=opc-1
        print(f"Ahora tu campeon es {champ[opc]}\n")
        input("Presione enter")
        system("cls")
    elif op ==2:
        while True:
            print("Que items va a comprar? (con 0 sale del programa)")
            for ti in range(len(ite)):
                print(f"{ti+1}.- {ite[ti]}")
            opt=int(input(">>> "))
            if opt==0:
                print("Saliendo")
                input("Precione enter")
                system("cls")
                break
            elif opt >=1 and opt<=8:
                opt=opt-1
                print(f"Se agrego {ite[opt]} con un coste de {pre[opt]}")
                car.append(opt)
                input("Presione enter")
                system("cls")
            else:
                print("Opcion invalida")
                input("Presione enter")
                system("cls")
    elif op == 3:
        with open("boleta lols>>.txt", "w") as archivo:
            archivo.write("--------------------------------\n")
            for p in car:
                car.sort()
                archivo.write(f"{ite[p]}---------{pre[p]}\n")
                to=to+ pre[p]
            archivo.write("--------------------------------\n")
            archivo.write(f"Su total es de ${to}\n")
            archivo.write("Es hora de volver a la grieta\n")
            archivo.write(f"Te deseamos suerte {champ[opc]}")
            
        print("--------------------------------")
        for p in car:
            car.sort()
            print(f"{ite[p]}---------{pre[p]}")
            to=to+pre[p]
        print("--------------------------------")
        print(f"Su total es de ${to}\n")
        print("Es hora de volver a la grietra")
        print(f"Te deseamos suete {champ[opc]}")
        break
    else:
        print("Opcion invalida")
        input("Presione enter")
        system("cls")