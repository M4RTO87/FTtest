from os import system
system("cls")

# edad=int(input("ingrese su edad: "))
# if edad <= 10:
#     print("su entrada es gratis")
# elif edad >10 and edad <19:
#     print("su entrada cuesta 1000")
# elif edad > 18 and edad <65:
#     print("su entrada cuesta 2000")
# else:
#     print("su entrda cuesta 1500")


# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# if num1 > num2:
#     print("El primer numero es mayor")
# if num2 > num1:
#     print("el segundo numero es mayor")

# num = int(input("Ingrese a multiplicar"))
# for i in range(10):
#     print(f"{num} x {i+1} = {num*(i+1)}")


# print("bienvenido")
# total= 0
# while True:
#     print("1.- ingrese su nombre")
#     print("2.- Menú de Platos")
#     print("3.- mostrar saludo")
#     print("4.- salir")
#     opc = int(input(">>> "))
#     if opc == 1 :
#         nom= input("ingresse su nombre\n >>>")
#         print(f"ahora su nombre se {nom}\n")
#     elif opc ==2:
#         while True:
#             print("menu del dia")
#             print("1.- Arroz a la francesa $4.500")
#             print("2.- Arroz marinero $5.200")
#             print("3.- Sopa marinera $9.700")
#             print("4.- volver al inicio")
#             op= int(input(">>> "))
#             if op ==1:
#                 print("se agrego Arroz a la francesa $4.500")
#                 total = total +4500
#             elif op==2:
#                 print("se agrego Arroz marinero $5.200")
#                 total = total +5200
#             elif op ==3:
#                 print("se agrego Sopa marinera $9.700")
#                 totl = total+9700
#             elif op ==4:
#                 print("volver al inicio")
#                 break
#             else:
#                 print("caracter invalido")
#     elif opc ==3:
#         print(f"hola {nom} por venir al restorant Panuchis")
#     elif opc ==4:
#         print("saliendo")
#         print(f"su total de la compra es de {total}")
#         print("gracias por su visita")
#         break


# num1 = int(input("ingrese el rango"))
# for i in range(num1+1):
#     if i%2==0:
#         print(f"los numeros positivos son: {i}")


import random
print("Bienvenido al juego de adivinar")
num1= int(input("ingrese la cantidad de intentos: "))
num = random.randint(1,20)
for i in range(num1):
        num1 = int(input("ingrese una numero: "))
        if num1 < num:
            print("el numero es muy bajo ")
        elif  num1 == num:
             print("corecto")
             break
        else:
            print("el numero en muy alto")