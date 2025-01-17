from os import system
system("cls")

import random
import sys
dado=random.randint(1,6)

def jug1():
    jug1=0
    print("turno de juagor 1")
    while True:
        dado=random.randint(1,6)
        da=input("va a tirar los dados? (si/no): ")
        if da == "si":
            jug1=jug1+dado
            print(f"saco un {dado}")
            print(f"ahora esta en la pisicion {jug1}\n")
        else:
            print("salto su turno")
            op=input("quiere salir (si/no)")
            if op=="si":
                print("saliendo termino el juego")
                sys.exit()
            else:
                print(" ")
    
def jug2():
        jug1=0
        jug2=0
        print("bienvenido a ludo")
        while True:
            dado=random.randint(1,6)

            da=int(input("va a tirar los dados jugador 1 ponga 1: "))
            if da == 1:
                jug1=jug1+dado
                print(f"saco un {dado}")
                print(f"ahora esta en la pisicion {jug1} de 24\n")
                if jug1 == 24:
                    print("gano jugador 1")
                    sys.exit()
                elif jug1 > 24:
                    print("su paso")
                print("jugardor 2 ahora es su turno")
                da=int(input("va a tirar los dadosjugardor 2 ponga 2: "))
                if da == 2:
                    jug2 =jug2+dado
                    print(f"saco un {dado}")
                    print(f"ahora esta en la pisicion {jug2} de 24\n")
                    if jug2 == 24:
                        print("gano jugador 2")
                        sys.exit()
                    elif jug2 > 24:
                        print("se paso")
                elif da !=2:
                    print("los dados se calleron de la mesa, tiralos bien")
            elif da != 1:
                print("los dados se calleron de la mesa, tiralos bien")
            

print("de cuantos jugadores quiere jugar 1/2")
op=int(input(">>> "))
match op:
    case 1:
        jug1()
    case 2:
        jug2()
    case _:
        print("opcion invalida")