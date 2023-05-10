# analisis del primer pacial de FP
V_cantEst = 1
C_valExaTeo = 0.40
C_valExaPra = 0.60
V_defPriPar = 0.0
V_conCic = 1
V_sumNotPriPar = 0.0
V_proNotPriPar = 0.0
V_sumNotFem = 0.0
V_sumNotMas = 0.0
V_proNotMas = 0.0
V_proNotFem = 0.0
V_NumFem = 0
V_NumMas = 0
V_sumNotTeo= 0.0 
V_sumNotPra= 0.0 
V_proNotPriTeo = 0.0
V_proNotPriPra = 0.0
V_sumNotTeoFem = 0.0 
V_sumNotPraFem= 0.0 
V_proNotPriTeoFem = 0.0
V_proNotPriPraFem = 0.0
V_sumNotTeoMas= 0.0 
V_sumNotPraMas= 0.0 
V_proNotPriTeoMas = 0.0
V_proNotPriPraMas = 0.0
v_notMax = 0.0
v_notMin = 5.0 
v_notMaxFem = 0.0
v_notMinFem = 5.0 
v_notMaxMas = 0.0
v_notMinMas = 5.0 
V_cantEst = int(input("digite la cantidad de destudiantes :"))
for V_conCic in range (V_cantEst):
    #captura de datos
    V_nomEst = input(" ingrese nombre del estudiante: ")
    V_genEst = int(input(" ingrese el genero del estudiante(1=masculino 2=femenino): "))
    V_notExaTeo = float(input(" ingrese nota del examen teorico: "))
    V_notExaPra = float(input(" ingrese nota del examen Practico: "))
    # Calculo de la nota del primer parcial
    V_defPriPar = V_notExaTeo * C_valExaTeo + V_notExaPra * C_valExaPra
    print ("su nota del primer parcial es :" , V_defPriPar)
    

    #calcular la suma de las notas de los estudiantes para calcular 
    V_sumNotPriPar = V_sumNotPriPar + V_defPriPar
    V_sumNotTeo= V_sumNotTeo + V_notExaTeo
    V_sumNotPra= V_sumNotPra + V_notExaPra
    #calcular la suma de las notas de los estudiantes por genero 
    if V_genEst==2:
        V_sumNotFem = V_sumNotFem + V_defPriPar
        V_NumFem = V_NumFem + 1
        V_sumNotTeoFem = V_sumNotTeoFem + V_notExaTeo
        V_sumNotPraFem = V_sumNotPraFem + V_notExaPra
        if V_defPriPar <= v_notMinFem:
            v_notMinFem = V_defPriPar
        if V_defPriPar >= v_notMaxFem:
         v_notMaxFem = V_defPriPar
    if V_genEst==1:
        V_sumNotMas = V_sumNotMas + V_defPriPar
        V_NumMas = V_NumMas + 1 
        print("en el ciclo llevo",V_NumMas)
        V_sumNotTeoMas = V_sumNotTeoMas + V_notExaTeo
        V_sumNotPraMas = V_sumNotPraMas + V_notExaPra
        if V_defPriPar <= v_notMinMas:
         v_notMinMas = V_defPriPar
        if V_defPriPar >= v_notMaxMas:
         v_notMaxMas = V_defPriPar
    #nota maxima
    
    
    if V_defPriPar <= v_notMin:
        v_notMin = V_defPriPar
    if V_defPriPar >= v_notMax:
        v_notMax = V_defPriPar
    
# Calcular promedio del grupo de las notas de primer parcial
V_proNotPriPar = V_sumNotPriPar/V_cantEst
print ("el promedio de notas es :" , V_proNotPriPar)
V_proNotPriTeo = V_sumNotTeo /V_cantEst
print ("el promedio de notas en el examen teorico es :" , V_proNotPriTeo)
V_proNotPriPra = V_sumNotPra /V_cantEst
print ("el promedio de notas en el examen practico es :" , V_proNotPriPra)
print ("la nota maxima fue  :" , v_notMax)
print ("la nota minima fue  :" , v_notMin)
# Calcular promedio del grupo de las notas de primer parcial por genero 
if V_NumMas > 0:
    print (V_NumMas)
    V_proNotMas = V_sumNotMas / V_NumMas 
    print ("el promedio de notas de los hombres es :" , V_proNotMas)
    V_proNotPriTeoMas = V_sumNotTeoMas /V_NumMas
    print ("el promedio de notas en el examen teorico en los hombres es :" , V_proNotPriTeoMas)
    V_proNotPriPraMas = V_sumNotPraMas /V_NumMas
    print ("el promedio de notas en el examen practico en los hombres es es :" , V_proNotPriPraMas)
    print ("la nota maxima en los hombres fue  :" , v_notMaxMas)
    print ("la nota minima en los hombres fue  :" , v_notMinMas)
if V_NumFem > 0:
    V_proNotFem = V_sumNotFem/ V_NumFem
    print ("el promedio de notas de las mujeres es :" , V_proNotFem)
    V_proNotPriTeoFem = V_sumNotTeoFem /V_NumFem
    print ("el promedio de notas en el examen teorico en las mujeres es :" , V_proNotPriTeoFem)
    V_proNotPriPraFem = V_sumNotPraFem /V_NumFem
    print ("el promedio de notas en el examen practico en las mujeres es :" , V_proNotPriPraFem)
    print ("la nota maxima en las mujeres fue  :" , v_notMaxFem)
    print ("la nota minima en las mujeres fue  :" , v_notMinFem)