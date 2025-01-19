from os import system
system("cls")
import time
import random
import sys
def dado():
    return random.randint(1,6)
jug1=0
jug2=0
jug3=0
jug4=0
pos1=0
pos2=0
pos3=0
pos4=0
va1=0
va2=0
va3=0
va4=0
v1=24
v2=24
v3=24
v4=24
def var1():
     global jug1
     global pos1
     global va1
     global v1
     pos1="◉ "*jug1
     va1="- "*v1
     print(f"jugador 1 {pos1}{va1} {jug1}/24")

def var2():
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

def var3():
    global jug1
    global jug2
    global jug3
    global pos1
    global pos2
    global pos3
    global va1
    global va2
    global va3
    global v1
    global v2
    global v3
    pos1="◉ "*jug1
    pos2="◉ "*jug2
    pos3="◉ "*jug3
    va1="- "*v1
    va2="- "*v2
    va3="- "*v3
    print(f"jugador 1 {pos1}{va1} {jug1}/24")
    print(f"jugador 2 {pos2}{va2} {jug2}/24")
    print(f"jugador 3 {pos3}{va3} {jug3}/24")

def var4():
    global jug1
    global jug2
    global jug3
    global jug4
    global pos1
    global pos2
    global pos3
    global pos4
    global va1
    global va2
    global va3
    global va4
    global v1
    global v2
    global v3
    global v4
    pos1="◉ "*jug1
    pos2="◉ "*jug2
    pos3="◉ "*jug3
    pos4="◉ "*jug4
    va1="- "*v1
    va2="- "*v2
    va3="- "*v3
    va4="- "*v4
    print(f"jugador 1 {pos1}{va1} {jug1}/24")
    print(f"jugador 2 {pos2}{va2} {jug2}/24")
    print(f"jugador 3 {pos3}{va3} {jug3}/24")
    print(f"jugador 4 {pos4}{va4} {jug4}/24")
    
def pla1():
    global jug1
    global pos1
    global va1
    global v1
    while True:
        for i in range(1):
            print(f"Turno del jugador {i+1}\n")
            tir=input("Precine (P) para tirar los dados\n>>> ")
            system("cls")
            if tir=="p":
                if i+1==1:
                    da=dado()
                    print(f"jugador 1 saco un {da}\n")
                    jug1=jug1+da
                    v1=v1-da
                    var1()
                    if jug1==24:
                        print("jugador 1 ganaste")
                        sys.exit()
                    elif jug1 >24:
                        print(f"jugador 1 saco un {da}\n")
                        jug1=jug1-da

def pla2():
    global jug1
    global jug2
    global pos1
    global pos2
    global va1
    global va2
    global v1
    global v2
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
                    var2()
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
                    var2()
                    if jug2==24:
                        print("jugador 2 ganaste")
                        sys.exit()
                    elif jug2 >24:
                        print(f"jugador 2 saco un {da}\n")
                        jug2=jug2-da

def pla3(): 
    global jug1
    global jug2
    global jug3
    global pos1
    global pos2
    global pos3
    global va1
    global va2
    global va3
    global v1
    global v2
    global v3  
    while True:
        for i in range(3):
            print(f"Turno del jugador {i+1}\n")
            tir=input("Precine (P) para tirar los dados\n>>> ")
            system("cls")
            if tir=="p":
                if i+1==1:
                    da=dado()
                    print(f"jugador 1 saco un {da}\n")
                    jug1=jug1+da
                    v1=v1-da
                    var3()
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
                    var3()
                    if jug2==24:
                        print("jugador 2 ganaste")
                        sys.exit()
                    elif jug2 >24:
                        print(f"jugador 2 saco un {da}\n")
                        jug2=jug2-da

                elif i+1==3:
                    da=dado()
                    print(f"jugador 3 saco un {da}\n")
                    jug3=jug3+da
                    v3=v3-da
                    var3()
                    if jug3==24:
                        print("jugador 3 ganaste")
                        sys.exit()
                    elif jug3 >24:
                        print(f"jugador 3 saco un {da}\n")
                        jug3=jug3-da

def pla4():
    global jug1
    global jug2
    global jug3
    global jug4
    global pos1
    global pos2
    global pos3
    global pos4
    global va1
    global va2
    global va3
    global va4
    global v1
    global v2
    global v3
    global v4
    while True:
        for i in range(4):
            print(f"Turno del jugador {i+1}\n")
            tir=input("Precine (P) para tirar los dados\n>>> ")
            system("cls")
            if tir=="p":
                if i+1==1:
                    da=dado()
                    print(f"jugador 1 saco un {da}\n")
                    jug1=jug1+da
                    v1=v1-da
                    var4()
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
                    var4()
                    if jug2==24:
                        print("jugador 2 ganaste")
                        sys.exit()
                    elif jug2 >24:
                        print(f"jugador 2 saco un {da}\n")
                        jug2=jug2-da

                elif i+1==3:
                    da=dado()
                    print(f"jugador 3 saco un {da}\n")
                    jug3=jug3+da
                    v3=v3-da
                    var4()
                    if jug3==24:
                        print("jugador 3 ganaste")
                        sys.exit()
                    elif jug3 >24:
                        print(f"jugador 3 saco un {da}\n")
                        jug3=jug3-da
                elif i+1==4:
                    da=dado()
                    print(f"jugador 4 saco un {da}\n")
                    jug4=jug4+da
                    v4=v4-da
                    var4()
                    if jug4==24:
                        print("jugador 4 ganaste")
                        sys.exit()
                    elif jug4 >24:
                        print(f"jugador 4 saco un {da}\n")
                        jug4=jug4-da

print("Hora de jugar Ludo")
op=int(input("De cuantos jugadores va a jugar (maximo 4)\n>>> "))
match op:
    case 1:
        pla1()
    case 2:
        pla2()
    case 3:
        pla3()
    case 4:
        pla4()
    case _:
        print("opccion invalida")
                