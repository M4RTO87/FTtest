from os import system
system("cls")

nom=["kayn","ekko","warwick","shaco"]
it=["mata craken","eclipse","danza","cuchilla oscura","rey arruinado","coleccionista"]
pre=[3000,3100,2500,3300,2900,3500]
car=[]
total=0
c=1

print("quien va a comprar")
for n in nom:
    print(f"{c}.- {n}")
    c=c+1
op=int(input(">>> "))
system("cls")

print(f"Bienvenido {nom[op-1]}\n")
while len(car)<5:
    print("que va a comprar (max 5 objetos)")
    for ti in range(len(it)):
        print(f"{ti+1}.- {it[ti]}")
    com=int(input(">>> "))-1
    print(f"se compro {it[com]} y su presio es de {pre[com]}\n")
    car.append(com)
    system("cls")
print("es hora de volver a la grieta del fornicador\n")
for t in car:
    print(f"{it[t]}__________________{pre[t]}")
    total=total+pre[t]
print(f"su total es de ${total} ahora a pelear {nom[op-1]}")
