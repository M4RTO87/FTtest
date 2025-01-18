from os import system
system("cls")
import random
import webbrowser

number = random.randint(1,20)

print("adivina el numero del 1 al 20")
inte=int(input("Cuantos intentos desea: "))

for i in range(inte):
    con=int(input("Ingrese el numero: "))
    if con == number:
        print("Es correcto")
        break
    if con < number:
        print("Es un numero mas alto")
    else:
        print("Es un numero mas bajo")
else:
    webbrowser.open("https://www.youtube.com/watch?v=QOhmcbfwxnA")
    print("Se acabaron los intentos")
    print("cagaste")
    