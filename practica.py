from os import system
system("cls")

#1
edad = int(input("ingrese su eda: "))
if edad > 10 and edad < 18:
    print("su entrda cuesta $1000")
elif edad > 17 and edad < 66:
    print("su entrada cuesta $2000")
elif edad > 65:
    print("su entrda cuesta $1500")
else:
    print("su entrada es gratis")

#2
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
if num1 > num2:
    print(f"el primer numero es el mayor que es {num1}")
if num2 > num1:
    print(f"el segundo numero es el mayor que es {num2}")


#3
mul = int(input("que tabla dese ver: "))
for i in range(10):
    print(f"{mul}x{i+1} = {mul*(i+1)}" )


# #3.1
mul = int(input("que tabla dese ver: "))
ran = int(input("de cuantos numero: "))
for i in range(ran):
    print(f"{mul}x{i+1} = {mul*(i+1)}" )

#3.2
print("tablas del 1 al 10")
for j in range(10):
    for i in range(10):
        print(f"{j+1}x{i+1} = {(j+1)*(i+1)}" )

#4
total=0
non="no ingresado"
print("Bienbenido")
while True:
    print("1.- Ingrese su nombre")
    print("2.- Mostrar menu de platos")
    print("3.- Mostrar saludo")
    print("4.- Salir\n")
    opc = int(input("Ingrese su opcion: "))
    if opc == 1:
        nom = input("Ingrese su nombre: ")
        print(f"Ahora su nombre es {nom}\n")
    elif opc == 2:
        while True:
            print("1.- Arroz a las brasas $4.500")
            print("2.- Arroz marinero $5.200")
            print("3.- Sopa marinera $9.700")
            print("4.- Salir\n")
            op = int(input("Ingrese su opccion: "))
            if op == 1:
                print("Se agrego Arroz a las brasas $4.500\n")
                total =total+4500
            elif op == 2:
                print("Se agrego Arroz marinero $5.200\n")
                total =total+5200
            elif op == 3:
                print("Se agrego Sopa marinera $9.700\n")
                total=total+9700
            elif op ==4:
                print("Saliendo, Gracias por su compra\n")
                break
            else:
                print("ingrse una opcion valida\n")
    elif opc == 3:
        print(f"Gracias {nom} por venir al restorant Panuchis\n")
    elif opc == 4:
        print(f"gracias por su visita su total es de ${total}\n")
        break
    else:
        print("Ingrese una opcion valida")