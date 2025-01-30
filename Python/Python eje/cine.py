from os import system
system("cls")

cine=[
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[]],
    ]
c=1
t=0
while True:
    print("1.- Ver sala de cine")
    print("2.- Comprar entrada")
    print("3.- Boleta")
    print("4.- Salir")
    op=int(input(">>> "))
    if op==1:
        for i in cine:
            print(f"Fila {c}\n{i}")
            c=c+1
        c=1
        input("\npresione enter para volver")
        system("cls")
    elif op==2:
        nom=input("Ingrese su nombre\n>>> ")
        f=int(input("que fila desea\n>>> "))
        print(f"Fila {f}\n{cine[f-1]}")
        a=int(input("que asiento desea\n>>> "))
        if cine[f-1][a-1] ==[]:
            cine[f-1][a-1]=[nom]
            print("Se guardo su aciento se guardo")
            print(f"Flia {f} asiento {a}")
            input("Precione enter para continuar")
            system("cls")
        else:
            print("esta acupado esta aciento")
    elif op==3:
        print("Fila  Asiento  Precio")
        print("---------------------------------")
        for i, fila in enumerate(cine):
            for j, asiento in enumerate(fila):
                if asiento:
                    if 0 <= i <= 3:
                        t=t+ 78500
                    elif 4 <= i <= 6:
                        t=t+ 90000
                    else:
                        t=t+ 110000
                    print(f"{i+1}      {j+1}       ${t}")
        print("---------------------------------")
        print(f"Total a pagar: ${t}")
        input("\nPresione enter para volver")
        system("cls")
        with open("entrada de cine.txt", "w") as archivo:
            archivo.write("Fila  Asiento  Precio\n")
            archivo.write("---------------------------------\n")
            for i, fila in enumerate(cine):
                for j, asiento in enumerate(fila):
                    if asiento:
                        if 0 <= i <= 3:
                            t=t+ 78500
                        elif 4 <= i <= 6:
                            t=t+ 90000
                        else:
                            t=t+ 110000
                        archivo.write(f"{i+1}      {j+1}       ${t}\n")
            archivo.write("---------------------------------\n")
            archivo.write(f"Total a pagar: ${t}\n")
    elif op ==4:
        print("Disfrute su funcion")
        break
    else:
        print("opccion invalida")