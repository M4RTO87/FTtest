from os import system
system("cls")

def deuda(pag):
    deu=100000
    #
    if pag == 0 or pag <= deu:
        deu=deu-pag
        print(f"ahora su deuda es de {deu}")
    else:
        print("monto invalido")


def compra():
    total=0
    while True:
        print("1.- comprar")
        print("2.- salir")
        op=int(input(">>> "))
        if op ==1:
            com=int(input("de cuanto es el costo del poducto\n>>> "))
            if com >=0:
                total=total+com
                print(f"ahora su total es de ${total}")
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
            pag=int(input("monto para realizar un pago"))
            deuda(pag)
        case 2:
            compra()
        case 3:
            print("saliendo")
            break
        case _:
            print("opccion invalida")