sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)

for x in range (4):
    if sueldos[x] > sueldos[x + 1]:
        aux=sueldos[x]
        sueldos[x] = sueldos[x + 1]
        sueldos[x + 1]=aux

for x in range (3):
    if sueldos[x] > sueldos[x + 1]:
        aux=sueldos[x]
        sueldos[x] = sueldos[x + 1]
        sueldos[x + 1]=aux

for x in range (2):
    if sueldos[x] > sueldos[x + 1]:
        aux=sueldos[x]
        sueldos[x] = sueldos[x + 1]
        sueldos[x + 1]=aux

for x in range (1):
    if sueldos[x] > sueldos[x + 1]:
        aux=sueldos[x]
        sueldos[x] = sueldos[x + 1]
        sueldos[x + 1]=aux

print (sueldos)
