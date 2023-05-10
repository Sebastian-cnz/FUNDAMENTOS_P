#leer un valor por teclado y buscarlo en la lista y eliminarlo
import random 
lista = []
valor= 0
for x in range(30):
    valor = random.randint(1, 99)
    lista.append(valor)
print (lista)
numE = int (input("ingrese valor a eliminar: "))
for x in range(30):
    if lista[x] == numE:
        lista[x] = lista [x + 1]
        lista.remove(x + 1)
print (lista)
