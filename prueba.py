from os import system
system("cls")

#1
edad = int(input("ingrese su edad: "))
if edad >10 and edad < 19:
    print("su boleto cuesta $ 1000")
if edad >18 and edad < 66:
    print("su bolet cuesta $2000")
if edad > 65:
    print("su entrada es de 1500")
if edad <=10:
    print("su entrada es gratis")

#2
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
if num1 < num2:
    print(f"el segundo numero que es {num2} es le mayor")
if num1 > num2:
    print(f"el primer numero que es {num1} es el mayor")

#3
num =int(input("ingrese el numero de la tabla deseada: "))
for mul in range (10):
        print(num,"x",mul+1,"=",((num)*(mul+1)))
        

#4
total=0
nom="nobre no ingresado"
while True:
    print("1.- ingrese su nombre")
    print("2.- mostrar menu de platos")
    print("3.- mostrar saludo")
    print("4.- salir\n")
    opc =int(input("ingrse su opccion: "))
    if opc == 1:
        nom=input("ingrese su nombre: ")
        print(f"ahora su nombre es {nom}\n")
    if opc ==2:
        while True:
            print("aqui esta el menu de platos")
            print("1.- arroz a la francesa $4.500")
            print("2.- arroz marinero $5.200")
            print("3.- sopa marinera $9.700")
            print("4.- salir")
            op=int(input("ingrse su opccion: "))
            if op == 1:
                total = total+4500
                print("se agrego arroz a la francesa $4.500\n")
            if op ==2:
                total =total+5200
                print("se agrego arroz marinero $5.200\n")
            if op == 3:
                total =total+9700
                print("se agrego sopa marinera $9.700\n")
            if op == 4:
                print("estas saliendo\n")
                break
            elif op > 4:
                print("ingrese una opccion valida\n")
    if opc ==3:
        print(f"Gracias {nom} por venir al restorant Panuchis\n")
    if opc ==4:
        print("hasta la proxima")
        print(f"su total es de ${total}")
        break
    elif opc > 4:
                print("ingrese una opccion valida\n")
