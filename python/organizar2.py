sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)
canInt = 0
for x in range(4):
    for x in range (4):
        if sueldos[x] > sueldos[x + 1]:
            aux=sueldos[x]
            sueldos[x] = sueldos[x + 1]
            sueldos[x + 1]=aux
            canInt = canInt + 1

print (sueldos)
print (canInt)