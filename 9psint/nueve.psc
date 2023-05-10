Algoritmo nueve
	
	//Area de  documentacion
	//enunciado: Escribir un algoritmo que acepte tres números enteros e imprima el mayor de ellos. 
	//version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir N1 como real //entrada 
	Definir N2 como real //entrada 
	Definir N3 como real //entrada 
	Definir P como real //salida 
	
	// area de inicialisacion de variables 
	N1 = 0.0 
	N2 = 0.0 
	N3 = 0.0
	P = 0.0
	
	//Area de entradas 
	escribir "digite el primer numero"
	leer N1
	escribir "digite el segundo numero"
	leer N2
	escribir "digite el tercer numero"
	leer N3
	
	//area de procesos 
	Si N1 > N2 Entonces
		Si N1 > N3 Entonces
			P = N1
		SiNo
			P = N3
		Fin Si
	Fin Si
	Si N2 > N3
		Si N2 > N1 Entonces
			P = N2
		SiNo
			P = N1
		Fin Si
	Fin Si
	si N3 > N1 entonces
			Si N3 > N2 Entonces
				P = N3
			SiNo
				P = N2
			Fin Si
	finsi
	Si N1 = N2 y N2 = N3 entonces 
		//area de salidas
		escribir "los numeros son iguales"
	sino 
		//area de salidas
		escribir P " es el numero mayor"
	FinSi
	
FinAlgoritmo
