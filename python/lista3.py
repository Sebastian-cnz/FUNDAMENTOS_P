menor = 0
lista = []
for x in range(5):
    valor = int (input("ingrese valor: "))
    lista.append(valor)

mayor = menor

for x in range (5):
    if lista[x] < menor :
        menor=lista[x]

print (lista)
print (mayor)
print (menor)