lista = []
valor = 0
while valor!= 0:
    valor = int (input("ingrese valor: "))
    lista.append(valor)

mayor= lista[0]

buscar = int(input("ingrese valor a buscar: "))

for x in range (valor):
    if lista [x] == buscar:
        print ("el numero esta") 
    else: 
        print("el numero no esta")
    
    

    
    
for x in range (1,5):
    if lista[x] > mayor:
        mayor=lista[x]

menor = mayor

for x in range (1,5):
    if lista[x] < menor:
        menor=lista[x]
        


print (lista)
print (mayor)
print (menor)

#leer un numero por teclado y respoder estas dos preguntas: esta o no esta? si esta cuantas veces se repite y en que posiciones? 