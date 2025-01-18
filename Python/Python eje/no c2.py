from os import system
system("cls")

import sys
nom=""
pw=""
while True:
    print("1.- Crear usuario")
    print("2.- iniciar secion")
    print("3.- Salir\n")
    opc= int(input(">>> "))
    if opc==1:
        print("Vamos a crear tu cuenta")
        nom=input("Ingresa tu nombre: \n")
        pw=input("ahora ingresa tu contraseña: \n")
        print(f"Hola {nom}")
    elif opc==2:
        while True:
            print("Inicia secion\n")
            nom1 =input("Ingrese tu usuario: \n")
            pw1 = input("Ingrese su contraseña: \n")
            if nom1 == nom and pw1 == pw:
                print("Bienvenido")
                sys.exit()
            else:
                print("Usuario o Contraseña incorrecta\n")
    elif opc ==3:
        print("Saliendo")
        break
    else:print("Caracter invalido")
