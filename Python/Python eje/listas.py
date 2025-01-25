from os import system
system("cls")

# par=[]
# inp=[]


# num=int(input("ingresa un número entero positivo : "))
# for i in range(num):
#     if i%2!=0:
#         par.append(i+1)
# for i in range(num):
#     if i%2==0:
#         inp.append(i+1)
        
# print(f"los pares son: {par}")
# print(f"los inpares son: {inp}")

# nota=[]
# while True:
#     no=int(input("ingrese su nota (con 0 sale del programa): "))
#     if no !=0:
#         nota.append(no)
#         print(f"la notas que tiene son\n{nota}")
#         suma=sum(nota)
#         can=len(nota)
#         pro=suma/can
#         print(pro)
#     else:
#         print("saliendo")
#         break    


# nom=[]
# for i in range(3):
#     no=input("ingrese su nombre y apellido: ")
#     print(f"el nombre ingresado tiene {len(no)} caracteres")
#     nom.append(no)
#     nom.sort()
    
# print(nom)
    
# import random
# lot=[]

# for i in range(7):
#     num=random.randint(1,38)
#     lot.append(num)
#     lot.sort()
# print(f"este es su carton {lot}")

colo=[]
u=[]
op=input("a que eqipo desea agregar (colo/u)")
if op =="colo":
    opc=int(input("ingrese el numero del jugador"))
    colo.append(opc)
    print(f"el equipo de colo quedo asi {colo}")
else:
    opc=int(input("ingrese el numero del jugador"))
    u.append(opc)
    print(f"el equipo de la u quedo asi {u}")