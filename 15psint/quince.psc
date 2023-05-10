Algoritmo quince
	//Area de  documentacion
	//enunciado: DDiseñar un programa que lea tres números A, B, C y visualice en pantalla el valor del más grande. Se supone que los tres valores son diferentes. 
	//version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir A como real //entrada 
	Definir B como real //entrada 
	Definir C como real //entrada 
	Definir R como real //salida 
	
	// area de inicialisacion de variables 
	A = 0.0 
	B = 0.0 
	C = 0.0
	R = 0.0
	
	//Area de entradas 
	escribir "digite el primer numero"
	leer A
	escribir "digite el segundo numero"
	leer B
	escribir "digite el tercer numero"
	leer C
	
	//area de procesos 
	Si A > B Entonces
		Si A > C Entonces
			P = A
		SiNo
			R = C
		Fin Si
	Fin Si
	Si B > C
		Si B > A Entonces
			P = B
		SiNo
			R = A
		Fin Si
	Fin Si
	si C > A entonces
		Si C > B Entonces
			P = C
		SiNo
			R = B
		Fin Si
	finsi
	Si A = B o B = C o C = A entonces 
		//area de salidas
		escribir "error los numero tienen que se diferentes "
	sino 
		//area de salidas
		escribir R " es el numero mayor"
	finsi
FinAlgoritmo
