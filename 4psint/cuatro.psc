Algoritmo cuatro
	//Area de  documentacion
	//enunciado: Se desea realizar el algoritmo que resuelva el siguiente problema: Cálculo de los salarios mensuales de los empleados de una empresa, sabiendo que éstos se calculan en base a las horas semanales trabajadas y de acuerdo a un precio especificado por horas. Si se pasan de cuarenta horas semanales, las horas extraordinarias se pagarán a razón de 1,5 veces la hora ordinaria. 
	//version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	
	Definir HS como real //entrada 
	Definir V como real //entrada 
	Definir N como real // proseso 
	Definir A como real //constante
	Definir S como real //salida 

	
	// area de inicialisacion de variables 
	HS = 0.0 
	V = 0.0 
	N = 0.0
	IM = 0.0 
	A = 1.5
	S = 0.0 
	
	//Area de entradas 
	escribir " escriba las horas trabajadas en la semana"
	leer HS
	escribir " escriba el valor por horas"
	leer v
	
	
	//area de procesos 
	Si HS > 40 Entonces
		N = HS - 40
		S <- HS * V 
		E = N * A 
		S = E + S
	SiNo
		S <- HS * V 
	Fin Si
	
	
	
	//area de salidas
	escribir " el salario es" S
FinAlgoritmo
