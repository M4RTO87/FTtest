from os import system
system("cls")

deu=100000
def deuda():
    pag=int(input("monto para realizar un pago"))
    if pag == 0 or pag <= deu:
        deu-pag
        print(f"ahora su deuda es de {deu-pag}")
    else:
        print("monto invalido")



def compra():
    while True:
        print("1.- comprar")
        print("2.- salir")
        op=int(input(">>> "))
        if op ==1:
            com=int(input("de cuanto es el costo del poducto\n>>> "))
            if com >=0:
                com+deu
                print(f"ahora su total es de ${deu+com}")
            else:
                print("monto invalido")
        elif op ==2:
            print("saliendo")
            break


while True:
    print("1.- pagar deuda")
    print("2.- comprar")
    print("3.- salir")
    op=int(input(">>> "))
    match op:
        case 1:
            deuda()
        case 2:
            compra()
        case 3:
            print("saliendo")
            break
        case _:
            print("opccion invalida")
