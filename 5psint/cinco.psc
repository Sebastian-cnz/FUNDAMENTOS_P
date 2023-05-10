Algoritmo cinco
	
	//Area de  documentacion
	//enunciado: Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta lo siguiente: toda llamada que dure menos de tres minutos (cinco pasos) tiene un coste de 10 céntimos, cada minuto adicional a partir de los tres primeros es un paso de contador y cuesta 5 céntimos. 
	//version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir m como real //entrada 
	Definir R como real //salida 
	definir C como real //constante 5
	Definir P como real // proseso 
	
	// area de inicialisacion de variables 
	m = 0.0 
	R = 0.0 
	c = 5
	P = 0.0
	//Area de entradas 
	escribir "digite los mituos de la llamada"
	leer m
	
	
	//area de procesos 
	Si m > 3 Entonces
		P = m - 3
		R = P * 5 + 10 
	SiNo
		R = 10 
	Fin Si
	
	//area de salidas
	escribir "el valor de la llamada son " R " centimos"
	
FinAlgoritmo