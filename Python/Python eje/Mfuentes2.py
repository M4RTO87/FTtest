from os import system
system("cls")

#ejercicio 1

total=0
while True:
    print("Bienvenido al supermerkado")
    print("1.- Comprar")
    print("2.- Pagar y Salir")
    opc=int(input(">>> "))
    if opc==1:
        while True:
            print("1.- Arroz $3150")
            print("2.- Aceite $1990")
            print("3.- Queso $2150")
            print("4.- Leche $1190")
            print("5.- volver al inicio")
            op= int(input(">>> "))
            if op==1:
                print("se agrego Arroz $3150")
                total=total+3150
            elif op==2:
                print("se agrego Aceite $1990")
                total=total+1990
            elif op==3:
                print("se agrego Queso $2150")
                total=total+2150
            elif op==4:
                print("se agrego Leche $1190")
                total=total+1190
            elif op==5:
                print("volviendo al inicio")
                break
            else:
                print("opcion no valida")
    elif opc==2:
        print(f"su total es de {total}")
        total1=total*1.19
        print(f"su total con iva incluido es ${total1}")
        break
    else:
        print("opcion no valida")


#ejercicio 2

# while True:
#     try:
#         edad=int(input("ingrese su edad\n>>> "))
#         if edad >=10 and edad <=80:
#             print("su edad esta en el rango permitido")
#             break
#         else:
#             print("el número ingresado está fuera del rango permitido")
#     except ValueError:
#         print("no es entero")
    

#ejercicio 3

# num=int(input("ingresa un número entero positivo : "))
# for i in range(num):
#     if i%2!=0:
#         print(f"los numero pares son {i+1}")   
# for i in range(num):
#     if i%2==0:
#         print(f"los numero impares son {i+1}")


#ejercicio 4

# nota=int(input("ingrese su nota: "))
# if nota <29:
#     print("su nota es una F")
# elif nota >=30 and nota<=39:
#     print("su nota es una D")
# elif nota >=40 and nota <= 49:
#     print("su nota es una C")
# elif nota >=50 and nota <= 64:
#     print("su nota es una B")
# else:
#     print("su nota es una A")