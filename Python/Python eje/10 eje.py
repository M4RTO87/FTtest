from os import system
system("cls")

#1
# for i in range(10):
#     print(f"N°.- {i+1}")

#2
# def fa_ite(n):
#     resultado = 1
#     for i in range(1, n + 1):
#         resultado *= i
#     return resultado
# def fa_recu(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fa_recu(n - 1)

# print(fa_ite(5))
# print(fa_recu(5))

#3
# fr=input("ingrese una frase\n>>> ")
# pa=fr.split()
# for i ,pa in enumerate(pa):
#     print(f" palabra {i+1}: {pa}")

#4
# n=int(input("de cuantos termino quiere: "))
# a,b=0,1
# print("susecion: ")
# for _ in range(n):
#     print(a, end=" ")
#     a,b=b,a+b

#5
# r=int(input("de cuantos pisos quiere el albol: "))
# for i in range(r):
#     print("*"*(i+1))

#6
# num=0
# while True:
#     op=int(input("ingrese el numero(con -1 se termina todo)\n>>> "))
#     if op != -1:
#         print(f"se sumo el N° {op}")
#         num=num+op
#     else:
#         print(f"su total es de {num}")
#         break

#7
# con="lol12"
# for i in range(4):
#     if i+1==1:
#         op=input("ingrese su contraseña: ")
#         if op==con:
#             print("corecto")
#             break
#         elif op != con:
#             print("incorecto")
#     if i+1==2:
#         op=input("ingrese su contraseña: ")
#         if op==con:
#             print("corecto")
#             break
#         elif op != con:
#             print("incorecto")
#     if i+1==3:
#         op=input("ingrese su contraseña: ")
#         if op==con:
#             print("corecto")
#             break
#         elif op != con:
#             print("incorecto")
#     if i+1==4:
#             print("llamando a la policia")
#             break

#8
# import math
# import sys
# while True:
#     ca1=int(input("ingrese el cateto a: "))
#     if ca1<0:
#         print("ingrese un cateto mayor que 0")
#     else:
#         print(f"su cateto a es {ca1}")
#         a=ca1
#         while True:
#             ca2=int(input("ingrese el cateto b: "))
#             if ca2<0:
#                 print("ingrese un cateto mayor que 0")
#             else:
#                 print(f"su cateto b es {ca2}")
#                 b=ca2
#                 print(f"el resultado de la hipotenuza es {math.sqrt(a**2 + b**2)}")
#                 sys.exit()

#9
# def num():
#     global b
#     global a
#     while True:
#         b1=int(input("ingrese el numero b: "))
#         if b1==0:
#             print("el numero b no puede ser 0")
#         elif b1!=0:
#             b=b1
#             print(f"el numero b es: {b}")
#             a1=int(input("ingrese el numero a: "))
#             a=a1
#             print(f"el numero a es: {a}")
#             break
# def cal():
#     while True:
#         print("1.- raiz cuadrada de la suma de a y b")
#         print("2.- deivide a/b")
#         print("3.- calcular (a*b)/2.5")
#         print("4.- salir")
#         op=int(input(">>> "))
#         if op ==1:
#             num=a+b
#             ra=num**(1/2)
#             print(f"la raiz cuadrada de la suma de a y b es {ra}")
#         elif op ==2:
#             div=a/b
#             print(f"la divicion de a/b es {div} ")
#         elif op ==3:
#             cal=(a*b)/2.5
#             print(f"el calculo de (a*b)/2.5 es {cal}")
#         elif op == 4:
#             print("saliendo")
#             break
# num()
# cal()

#10
import random
import sys
def ran():
    return random.randint(1,2)
jug1 = 60
jug2 = 60
ra=ran
input("presione enter para jugar")
while True:
    for ra in range(2):
        if ra==1:
            print("ataca el jugador 1")
            jug2=jug2-10
            print(f"la vida del jugador 2 queda en {jug2}")
            if jug2<=0:
                print("gana el jugador 1")
                sys.exit()
            elif jug2 >0:
                print("turno del siguiente jugador")
        if ra==2:
            print("ataca el jugador 2")
            jug1=jug1-10
            print(f"la vida del jugador 1  queda en {jug1}")
            if jug1 <=0:
                print("jaga el jugador 2")
                sys.exit()
            elif jug1 >0:
                print("turno del siguiente jugador")
