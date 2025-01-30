from os import system
system("cls")
c=1
     #a1   a2  a3 a4  a5  a6
     #0    1   2  3   4   5
hotel=[
    [["1"], [], [],[], [], []], #p1=0
    [["2"], [], [],[], [], []], #p2=1
    [["3"], [], [],[], [], []], #p3=2
    [["4"], [], [],[], [], []], #p4=3
    [["5"], [], [],[], [], []], #p5=4
    [["6"], [], [],[], [], []], #p6=5
    [["7"], [], [],[], [], []], #p7=6
    [["8"], [], [],[], [], []], #p8=7
    [["9"], [], [],[], [], []], #p9=8
    [["10"], [], [],[], [], []], #p10=9
]

while True:
    print("Bienvenido al hotel mamitas")
    print("1.- Agregar un habitacion")
    print("2,. Ver estado del hotel")
    print("3.- Sacar una havitacion")
    print("4.- Salir")
    op=int(input(">>> "))
    if op==1:
        nom=input("ingrese su nombre\n>>> ")
        print("que piso desea agendar")
        opp=int(input(">>> "))
        print(f"Piso {opp}")
        print(f"{hotel[opp-1]}\n")
        opa=int(input("que avitacion desea\n>>> "))
        if hotel[opp-1][opa-1]==[]:
            hotel[opp-1][opa-1]=[nom]
            print(f"{nom} se agendo su abitacion")
            print(f"Piso {opp} Abitacion {opa}")
        else:
            print("ta ocupao")
    elif op==2:
        for h in hotel:
            print(f"Piso {c}\n{h}\n")
            c=c+1
        c=1
    elif op ==3:
        print("que abitacion desea dessoccupar")
        print("seccione piso")
        opdp=int(input(">>> "))
        print(f"Piso {opdp}\n{hotel[opdp-1]}")
        opda=int(input("que abitacion desea dessoccupar\n>>> "))
        if hotel[opdp-1][opda-1]!=[]:
            hotel[opdp-1][opda-1]=[]
            print("abitacion desocupada\n")
        else:
            print("esta abitacion esta desocupada")
        
