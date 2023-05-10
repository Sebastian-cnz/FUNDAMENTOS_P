#leer un numero por teclado y respoder estas dos preguntas: esta o no esta? si esta cuantas veces se repite y en que posiciones? 
lista=[]
lisPosRep = []
valor = int(input("ingrse valor (0 para finalizar):"))
while valor!= 0:
    lista.append(valor)
    valor=int(input("ingrse valor (0 para finalizar):"))

print("tamaño de la lista: ")
print(len(lista))
print(lista)

valBus=int(input("pedir dato a buscar: "))

posLis= 0
canEleRep = 0

while posLis <int(len(lista)):
 if lista [posLis]== valBus:
    canEleRep = canEleRep + 1
    lisPosRep.append(posLis)

    posLis = posLis+1
