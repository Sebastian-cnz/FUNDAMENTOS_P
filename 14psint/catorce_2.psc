Algoritmo catorce_2
	//Area de  documentacion
	//enunciado: Preguntar qué día de la semana fue el día 1 del mes actual y calcular que día de la semana es hoy. 
	//version:2.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir diaDelMes como Entero
	Definir primerDia como Entero
    Definir dias Como Caracter
	Definir primerDiaDelMes Como Caracter
	
	// area de inicialisacion de variables 
	diaDelMes = 0
	primerDia = 0 
	dias = ""
	primerDiaDelMes = ""
	
	//Area de entradas 
    dimension dias[8]
    dias[2] = "lunes"
    dias[3] = "martes"
    dias[4] = "miercoles"
    dias[5] = "jueves"
    dias[6] = "viernes"
    dias[7] = "sabado"
    dias[8] = "domingo"
    Escribir "Ingrese el primer dia del mes: (lunes, martes, miercoles, jueves, viernes, sabado, domingo)"
    leer primerDiaDelMes
    Escribir "Ingrese que dia del mes quiere saber"
    Leer diaDelMes
	
	//area de procesos 
    si (primerDiaDelMes == "lunes") Entonces
        primerDia = 0
    SiNo
        Si (primerDiaDelMes == "martes") Entonces
            primerDia = 1
        SiNo
            Si (primerDiaDelMes == "miercoles") Entonces
                primerDia = 2
            SiNo
                Si (primerDiaDelMes == "jueves") Entonces
                    primerDia = 3
                SiNo
                    Si (primerDiaDelMes == "viernes") Entonces
                        primerDia = 4
                    SiNo
                        Si (primerDiaDelMes == "sabado") Entonces
                            primerDia = 5
                        SiNo
                            primerDia = 6
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
	
	//area de salidas
    Escribir(dias[(((diaDelMes + primerDia)%7) + 1)])
FinAlgoritmo
