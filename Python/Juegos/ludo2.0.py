from os import system
system("cls")
import time
import random
import sys
jug1=0
jug2=0
pos1=0
pos2=0
va1=0
va2=0
v1=24
v2=24
def dado():
    return random.randint(1,6)
def jug():
    global jug1
    global jug2
    global pos1
    global pos2
    global va1
    global va2
    global v1
    global v2
    pos1="◉ "*jug1
    pos2="◉ "*jug2
    va1="- "*v1
    va2="- "*v2
    print(f"jugador 1 {pos1}{va1} {jug1}/24")
    print(f"jugador 2 {pos2}{va2} {jug2}/24")
while True:
    for i in range(2):
        print(f"Turno del jugador {i+1}\n")
        tir=input("Precine (P) para tirar los dados\n>>> ")
        system("cls")
        if tir=="p":
            if i+1==1:
                da=dado()
                print(f"jugador 1 saco un {da}\n")
                jug1=jug1+da
                v1=v1-da
                jug()
                if jug1==24:
                    print("jugador 1 ganaste")
                    sys.exit()
                elif jug1 >24:
                    print(f"jugador 1 saco un {da}\n")
                    jug1=jug1-da

            elif i+1==2:
                da=dado()
                print(f"jugador 2 saco un {da}\n")
                jug2=jug2+da
                v2=v2-da
                jug()
                if jug2==24:
                    print("jugador 2 ganaste")
                    sys.exit()
                elif jug2 >24:
                    print(f"jugador 2 saco un {da}\n")
                    jug2=jug2-da