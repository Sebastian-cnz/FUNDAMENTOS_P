import random 
lista = []
listaCont = []
valor= 0
Cont = 0
aux = 0
for x in range(30):
    valor = random.randint(1, 20)
    lista.append(valor)
for x in range (30):
    if lista[x] > lista[x + 1]:
        aux=lista[x]
        lista[x] = lista[x + 1]
        lista[x + 1]=aux
        for x in range (30):
          if lista[x] == aux:
              Cont = Cont +1
              listaCont.append(Cont)
print(lista)
print(listaCont)
