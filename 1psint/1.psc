Algoritmo uno
	
	//Area de  documentacion
	//enunciado: Calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, número de horas trabajadas, impuestos a pagar y salario neto. 
	//version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir H como real //entrada 
	Definir V como real //entrada 
	Definir IM como real //entrada 
	Definir SB como real //salida 
	definir SN como real //salida
	
	// area de inicialisacion de variables 
	H = 0.0 
	V = 0.0 
	IM = 0.0 
	SB = 0.0 
	SN = 0.0 
	
	//Area de entradas 
	escribir " escriba las horas trabajadas"
	leer H
	escribir " escriba el valor por hora "
	leer v
	escribir " escriba el valor de los impuestos"
	leer IM
	
	//area de procesos 
	SB <- H * V 
	SN <- SB - IM
	
	//area de salidas
	escribir " Su salario bruto es" SB
	escribir " Su salario neto es" SN

FinAlgoritmo
