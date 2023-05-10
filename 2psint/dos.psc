Algoritmo dos
	//Area de  documentacion
	//enunciado: Calcular la media de una serie de números positivos, suponiendo que los datos se leen desde un terminal. Un valor de cero ?como entrada? indicará que se ha alcanzado el final de la serie de números positivos. 
	//version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir N como real //entrada 
	Definir C como real // proceso 
	Definir T como real // proceso 
	Definir P como real // salida
	
	// area de inicialisacion de variables 
	N= 0.0 
	R = 0.0 
	T = 0.0 
	
	//Area de entradas 
	escribir "ingrese los numeros positivos a los que quiera sacar la media, para finalizar ingrese 0"
	leer N
	Si N > 0 Entonces
		Mientras N > 0 Hacer
			T = N + T
			escribir "ingrese un numero positivo"
			leer N
			C = C + 1 
		Fin Mientras
		//area de procesos 
		R = T/C
		//area de salidas
		escribir "el promedio de los numeros ingresados es " R    
	SiNo
		escribir "solo se admiten numeros positivos"
	Fin Si
	

FinAlgoritmo
