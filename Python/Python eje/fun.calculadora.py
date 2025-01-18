from os import system
system("cls")

def suma():
    nu1=int(input("N° "))
    nu2=int(input("N° "))
    print(nu1+nu2)
    
def res():
    nu1=int(input("N° "))
    nu2=int(input("N° "))
    print(nu1-nu2)
    
def mul():
    nu1=int(input("N° "))
    nu2=int(input("N° "))
    print(nu1*nu2)
    
def div():
    nu1=int(input("N° "))
    nu2=int(input("N° "))
    print(nu1/nu2)
    
    
while True:
    print("""
          1.- suma
          2.- resta
          3.- multi
          4.- divi
          5.- salir""")
    op=int(input(">>> "))
    match op:
        case 1:
            suma()
        case 2:
            res()
        case 3:
            mul()
        case 4:
            div()
        case 5:
            break
        case _:print("invalid")
