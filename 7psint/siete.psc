Algoritmo siete
	
	//Area de  documentacion
	//enunciado: Escribir un algoritmo que calcule el producto de los n primeros números naturales. 
	//version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir N como entero //entrada 
	Definir P como entero // proceso 
	Definir R como entero //salida 
	
	
	// area de inicialisacion de variables 
	R = 0
	N = 0
	
	//Area de entradas 
	escribir "ingrese la cantidad de naturales a sumar"
	leer N
	
	//area de procesos 
	para P = 1 Hasta N Con Paso 1 Hacer
		R = R + P
	FinPara
	
	//area de salidas
	escribir R " es el producto de los primeros " N " numeros naturales"
	
FinAlgoritmo
