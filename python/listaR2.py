#leer un valor por teclado y buscarlo en la lista, si lo encuentra reemplazarlo por -1
import random 
lista = []
valor= 0
for x in range(30):
    valor = random.randint(1, 99)
    lista.append(valor)
print (lista)
numB = int (input("ingrese valor a buscar: "))
for x in range(30):
    if lista[x] == numB:
        lista[x]= -1
print (lista)

