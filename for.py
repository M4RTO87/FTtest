from os import system
system("cls")
# 1 tabla de multiplicar
# num = 2
# for i in range(10):
#     print(num,"x",i+1,"=",(i+1)*num)

#2
# tablas del 1 al 10   
# for j in range(10):
#     for i in range(10):
#         print(j+1,"x",i+1,"=",(i+1)*(j+1))

#3
# for i in range(19):
#     print("su edad es",i+1,"años")

#4 promedio
# total = 0
# for i in range(3):
#     print("ingrese una nota")
#     nota= int(input())
#     total=total+nota
# print("su promedio es",total/(i+1))

#5
# num =9
# if num%2==0:
#     print("el numero es par")
# else:
#     print("el numero es impar")

#6
# num= int(input("ingrese un numero: "))
# for i in range(num+1):
#     if i%2!=0:
#         print("el numero",i,"no es par")

#7
# for i in range(3):
#     con=input("ingrese cntraseña: ")
#     if con == "1234":
#         print("bienvenido")
#         break
#     else:
#         print("la contraseña es incorrecta")

#malo
for i in range(10):
    con=input("ingrese el numero: ")
    if con == 64:
        print(" es correcto")
        break
    if con > 64:
        print("es un numero mal alto")
    if con< 64:
        print("es un numero mas bajo")


inte=int(input("Cuantos intentos desea: "))

for i in range(inte):
    con=int(input("Ingrese el numero: "))
    if con == 64:
        print("Es correcto")
        break
    if con < 64:
        print("Es un numero mas alto")
    else:
        print("Es un numero mas bajo")
else:
    print("Se acabaron los intentos")
