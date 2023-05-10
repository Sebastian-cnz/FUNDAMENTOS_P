Algoritmo doce
	//Area de  documentacion
	//enunciado:Programa que nos calcule el área de un triángulo conociendo sus lados. 
	//version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	definir L1 Como Real //entrada 
	definir L2 Como Real //entrada 
	definir L3 Como Real //entrada 
	definir SP Como Real //proceso
	definir A como real //salida 
	
	// area de inicialisacion de variables 
	L1=0.0
	L2=0.0
	L3=0.0
	A=0.0
	SP=0.0
	//Area de entradas
	escribir "digite el lado 1"
	leer L1
	escribir "digite el lado 2"
	leer L2
	escribir "digite el lado 3"
	leer L3 
	
	//area de procesos 
	SP = (L1+L2+L3)/2
	A = Raiz(SP*(SP-L1)*(SP-L2)*(SP-L3))
	
	//area de salidas
	
	escribir "el area es igual a " A;
FinAlgoritmo
