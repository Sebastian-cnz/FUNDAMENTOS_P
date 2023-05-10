Algoritmo trece
	//Area de  documentacion
	//enunciado: Leída una fecha, decir el día de la semana, suponiendo que el día 1 de dicho mes fue lunes
	//version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir F como entero //entrada 
	Definir N como entero //proceso
	

	// area de inicialisacion de variables 
	F = 0
	N = 0
	
	
	//Area de entradas 
	escribir "digite la fecha"
	leer F
	
	
	//area de procesos 
	N = F % 7

	//area de salidas
	si N = 1
		escribir "el dia es lunes "
	FinSi
	si N = 2
		escribir "el dia es martes "
	FinSi
	si N = 3
		escribir "el dia es miercoles "
	FinSi
	si N = 4
		escribir "el dia es jueves "
	FinSi
	si N = 5
		escribir "el dia es viernes "
	FinSi
	si N = 6
		escribir "el dia es sabado "
	FinSi
	si N = 7
		escribir "el dia es domingo "
	FinSi
FinAlgoritmo
