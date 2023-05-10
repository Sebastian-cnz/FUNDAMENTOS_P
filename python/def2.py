def mostrar_mayor (v1, v2, v3):
    print("el mayor de los tres numeroes")
    if v1>v2 and v1> v3:
        print(v1)
    else:
        if v2>v3:
            print (v2)
        else: 
            print (v3)

def cargar():
    v1=int(input("ingrese el primer valor:"))
    v2=int(input("ingrese el segundo valor:"))
    v3=int(input("ingrese el tercer valor:"))
    mostrar_mayor(v1, v2, v3)