from os import system
system("cls")


import random
jug1=60
jug2=60
p1="2"
p2="r"
def atack():
     return random.randint(2,10)
at=atack()

def perso():
    while True:
        print("Street Fighter II: The World Warrior")
        print("1.- jugador 1 eliga personaje")
        print("2.- jugador 2  eliga personaje")
        print("3.- jugar")
        opc = int(input(">>> "))
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
                    break
                elif op ==2:
                    p1 ="Sagat"
                    print(f"jugador 1 eligiste a {p1}")
                    break
                elif op ==3:
                    p1="Ken"
                    print(f"jugador 1 eligiste a {p1}")
                    break
                elif op ==4:
                    p1="Chun-Li"
                    print(f"jugador 1 eligiste a {p1}")
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
                    print(f"jugador 1 eligiste a {p2}")
                    break
                elif op ==2:
                    p2 ="Sagat"
                    print(f"jugador 1 eligiste a {p2}")
                    break
                elif op ==3:
                    p2="Ken"
                    print(f"jugador 1 eligiste a {p2}")
                    break
                elif op ==4:
                    p2="Chun-Li"
                    print(f"jugador 1 eligiste a {p2}")
                    break
                else:
                    print("opcion invalida")
        elif opc ==3:
            print("a jugar")
            break
        else:
            print("opccion invalida")
def jueg():
    print("Pelea")
    print("Que jugador atacara? ")
    while True:
           print("1.- jugador 1")
           print("2.- jugador 2")
           op=int(input(">>> "))
           if op ==1:
               print("ataque del jugador 1")
               
         
         
def juego():
    print("Pelea")
    while True:
        print("")
        print("jugador 1 golpea")
        print("presione 1 golpear")
        at1=int(input(">>> "))
        if at1==1:
            print(f"la vida vajo {at} queda {jug2-at}")
        else:
            print("fallo ataque")
        print("ataque de jugador 2")
        print("presione 2 golpear")
        at2=int(input(">>> "))
        if at2==2:
            print("preparando ataque")
            print(f"la vida vajo {at} queda {jug1-at}")
            
        
        
        


op=int(input("presione 1 para jugar"))
match op:
    case 1:
        perso()
        print(p1)
        print(p2)
        juego()
    case 2:
        juego()