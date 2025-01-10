from os import system
system("cls")


# taco=1 
# pizza=2
# humitas=3
# cazuela=4
# print("elija una opccion de comida")
# print("""tacos=1
# pizza=2
# humitas=3
# cazuela=4""")

# op=int(input())

# if op ==(1):
#     print("Usted prefiere tacos")
# elif(op==(2)):
#     print("usted prefiere pizza")
# elif(op==(3)):
#     print("usted prefire humitas")
# elif(op==(4)):
#     print("usted prefiere cazuela")
# else:
#     print("usted es mañoso")
    
    
# num = 7
# def ver_par():
#     if num >0 and num%2==0:
#         print("elnumero es positivo y par")
#     else:
#         print("el numero es positivo y no es par")

# comida=100
# print("el plato esta lleno")
# while comida != 0:
#     comer = input("quiere comer (si/no)")
#     if comer == "si":
#         comida = comida-25
#         system("cls")
#     if comida == 0:
#         print("ya terminaste de comer")
#         break
#     else:
#         print(f"aun queda {comida}% del plato ")


        
        
num=0
print("numeros")
while num != 1:
    nume = int(input("ingrese un numero: "))
    if nume !=1:
        num = num+nume
    else:
        print(f"la suma tutal es de {num} ")
        break

    
