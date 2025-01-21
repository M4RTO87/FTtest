from os import system
system("cls")
con="lol12"
op=input("presione (D) para desbloquear el celular\n>>> ")
for i in range(4):
    if op=="d":
        if i+1==1:
            co=input("ingrese su contraseña\n>>> ")
            if co==con:
                print("contraseña corecta")
                break
            elif co!=con:
                print("contraseña incorecta")
        if i+1==2:
            co=input("ingrese su contraseña\n>>> ")
            if co ==con:
                print("contraseña corecta")
                break
            elif co !=con:
                print("contraseña incorecta")
        if i+1==3:
            co=input("ingrese su contraseña\n>>> ")
            if co ==con:
                print("contraseña corecta")
                break
            elif co!=con:
                print("contraseña incorecta")
        if i+1==4:
            print("se acavaro los intento")
            break
