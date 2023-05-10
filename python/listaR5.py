import random 
lista = []
valor= 0
Cont = 0
for x in range(30):
    valor = random.randint(1, 20)
    lista.append(valor)
print(lista)
num = int(input("ingrese valor que quiere saver cuanto se repite: "))
for x in range (30):
        if lista[x] == num:
              Cont = Cont +1 
print("el numero se repite",Cont)