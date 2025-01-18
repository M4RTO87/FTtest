from os import system
system("cls")

# 1
# # num=int(input("ingrese un numero: "))
# # for i in range(num):
# #     num=num-1
# #     print(f"quedan {num+1}")
# #     if num ==0:
# #         print("ya no quedan numeros")




# 2
# num1=int(input("ingrese el primer numero: "))
# num2=int(input("ingrese el segundo numero: "))
# num3 =int(input("ingrese el trcer numero: \n"))
# if num1>num2 and num1>num3:
#     print(f"el numero mayor de los 3 es {num1}")
# elif num2>num1 and num2>num3:
#     print(f"el numero mayor de los 3 es {num2}")
# else:
#     print(f"el numero mayor de los 3 es {num3}")
   
 
    
# 3
# num=int(input("ingres el numero a multiplicar: "))
# for i in range(10):
#     print(f"{num} x {i+1} = {num*(i+1)}")



#4
total=0
while True:
    print("1.- ingrese su nombre")
    print("2.- menu de platos")
    print("3.- total de la boleta")
    print("4.- salir")
    opc=int(input(">>> "))
    if opc ==1:
        nom=input("ingrese su nombre: ")
        print(f"ahora su nombre es {nom}")
    elif opc ==2:
        while True:
            print(" menu de platos")
            print("1.- Arroz a la francesa $4.500")
            print("2.- Arroz marinero $5.200")
            print("3.- Sopa marinera $9.700")
            print("4.- volver al inicio")
            op=int(input(">>> "))
            if op ==1:
                print("se agrego Arroz a la francesa $4.500\n")
                total=total+4500
            elif op ==2:
                 print("se agrego  Arroz marinero $5.200\n")
                 total=total+5200
            elif op ==3:
                 print("se agrego Sopa marinera $9.700")
                 total = total+9700
            elif op ==4:
                print("volviendo al inicio")
                break
            else:
                print("opcion invalida")
    elif opc==3:
        print(f"{nom} el total de su boleta es ${total}")
    elif opc ==4:
        print("saliendo, gracias por su visita")
        break
    else:
        print("opcion invalida")