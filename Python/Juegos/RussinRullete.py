from os import system
system("cls")

import random

def ruleta():
    return random.randint(1,6)

print("el que se mate primero pierde")
bala=ruleta()

for i in range(6):
    print(f"turno de jugardo {i+1}")
    print("para despara precione (g)")
    bal=input(">>> ")
    if bal =="g":
        if i+1 ==bala:
            print("cagaste")
            break
        else:
            print("vive otro asqueroso dia")
    else:
        print("digito invalido")