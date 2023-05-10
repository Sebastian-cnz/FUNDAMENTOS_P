Algoritmo tres
	//Area de  documentacion
	//enunciado: Suma de los números pares comprendidos entre 2 y 100. 
	//version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir N como entero //proceso 
	Definir S como entero //Salida
	
	
	// area de inicialisacion de variables 
	 S = 0
	
	
	//Area de entradas 
	
	
	//area de procesos 
	 para N = 2 Hasta 100 Con Paso 1 Hacer
		 si N mod 2 = 0 Entonces
			 S = S + N
		 FinSi
	 FinPara
	 

	//area de salidas
	Escribir "La suma de los números pares es: ",S
	

FinAlgoritmo
