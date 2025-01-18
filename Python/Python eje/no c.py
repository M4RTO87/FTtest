from os import system
system("cls")

#1
# con = input("ingrse su contaseña: ")
# pw = input("ferifique su contraseña: ")
# while True:
#     if pw != con:
#         print("La contasela es incorrecta")
#         pw= input("ingrese la contaseña: ")
#     elif pw == con:
#         print("Bienbenido")
#         break

#2
# import random
# print("Bienvenido al juego de adivinar")
# num1= int(input("ingrese la cantidad de intentos: "))
# num = random.randint(1,20)
# for i in range(num1):
#         num1 = int(input("ingrese una numero: "))
#         if num1 < num:
#             print("el numero es muy bajo ")
#         elif  num1 == num:
#              print("corecto")
#              break
#         else:
#             print("el numero en muy alto")


cog=870000
print("binvenido al bnaco")
while True:
        print("1.- ver monto")
        print("2.- sacar monto")
        print("3.- ingresar monto")
        print("4.- salir\n")
        opc = int(input("ingrese opccion: "))
        if opc ==1:
                print(f"su monto es de {cog}\n")
        elif opc ==2:
                while True:
                        ret=int(input("cuanto desea retirar: "))
                        if ret > cog :
                                print("ingrese un numero valido\n")
                        elif ret <= cog :
                                cog = cog-ret
                                print(f"ahora su saldo es de {cog}\n")
                                break
        elif opc == 3:
                while True:
                        reg=int(input("cunato desea depositar: "))
                        if reg < 1:
                                print("ingresse un numero valido")
                        elif reg >0:
                                cog=cog+reg
                                print(f"ahora su aldo es de ${cog}")
                                break
        elif opc == 4:
                print("gacias por visitar banco tula")
                break
        else:
                print("ingrese un caracter valido")
