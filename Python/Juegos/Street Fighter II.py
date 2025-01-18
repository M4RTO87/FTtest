from os import system
system("cls")
import time
import random
import sys
import math
jug1=60
jug2=60
p1=" "
p2=" "
ba1=0
ba2=0

def atack():
     return random.randint(2,10)
def critico():
    return random.randint(1,5)
def barra():
    global jug1
    global jug2
    global ba1
    global ba2
    ba1="/"*jug1
    ba2="/"*jug2

    print(f"{p1} - {ba1} - HP {jug1}/60")
    print(f"{p2} - {ba2} - HP {jug2}/60")
def perso():
    global p1
    global p2
    while True:
        print("Street Fighter II: The World Warrior")
        print("1.- jugador 1 eliga personaje")
        print("2.- jugador 2  eliga personaje")
        print("3.- jugar")
        opc = int(input(">>> "))
        system("cls")
        if opc ==1:
            print("jugador 1 seleccione su personaja")
            while True:
                print("1.- Ryu")
                print("2.- Sagat")
                print("3.- Ken")
                print("4.- Chun-Li")
                op=int(input(">>> "))
                if op == 1:
                    p1="Ryu"
                    print(f"jugador 1 eligiste a {p1}")
                    time.sleep(2)
                    system("cls")
                    break
                elif op ==2:
                    p1 ="Sagat"
                    print(f"jugador 1 eligiste a {p1}")
                    time.sleep(2)
                    system("cls")
                    break
                elif op ==3:
                    p1="Ken"
                    print(f"jugador 1 eligiste a {p1}")
                    time.sleep(2)
                    system("cls")
                    break
                elif op ==4:
                    p1="Chun-Li"
                    print(f"jugador 1 eligiste a {p1}")
                    time.sleep(2)
                    system("cls")
                    break
                else:
                    print("opcion invalida")
        elif opc ==2:
            print("jugador 2 seleccione su personaje")
            while True:
                print("1.- Ryu")
                print("2.- Sagat")
                print("3.- Ken")
                print("4.- Chun-Li")
                op=int(input(">>> "))
                if op == 1:
                    p2="Ryu"
                    print(f"jugador 2 eligiste a {p2}")
                    time.sleep(2)
                    system("cls")
                    break
                elif op ==2:
                    p2 ="Sagat"
                    print(f"jugador 2 eligiste a {p2}")
                    time.sleep(2)
                    system("cls")
                    break
                elif op ==3:
                    p2="Ken"
                    print(f"jugador 2 eligiste a {p2}")
                    time.sleep(2)
                    system("cls")
                    break
                elif op ==4:
                    p2="Chun-Li"
                    print(f"jugador 2 eligiste a {p2}")
                    time.sleep(2)
                    system("cls")
                    break
                else:
                    print("opcion invalida")
        elif opc ==3:
            break
        else:
            print("opccion invalida")

perso()
print("FIGHT!!!!!\n")
barra()
while True: 
    for i in range(2):
        print(f"Turno del jugador {i+1}\n")
        p =input("Precione (P) para atacar\n>>> ")
        system("cls") 
        if p=="p":
            if i+1==1:
                cri=critico()
                at=atack()
                if cri ==critico():
                    print("GOLPE CRITICOOO!!!!!\n")
                    at=at*math.ceil(1.6)
                print(f"la vida vajo {at}")
                jug2 = jug2-at
                barra()
                if jug2<=0:
                    time.sleep(1)
                    print("K.O")
                    time.sleep(1)
                    print(f"{p1} GANA")
                    sys.exit()
            if i+1==2:
                cri=critico()
                at=atack()
                if cri ==critico():
                    print("GOLPE CRITICOOO!!!!!\n")
                    at=at*math.ceil(1.6)
                print(f"la vida bajo {at}")
                jug1=jug1-at
                barra()
                if jug1<=0:
                    time.sleep(1)
                    print("K.O")
                    time.sleep(1)
                    print(f"{p2} GANA")
                    sys.exit()
