Algoritmo once
	//Area de  documentacion
	//enunciado: Se desea obtener la nómina semana, salario neto? de los empleados de una empresa cuyo trabajo se paga por horas
	//version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	definir v_nomEmp Como Caracter
	definir V_horSemTra Como entero 
	definir V_valHor  Como entero 
	definir V_valHorExt Como entero 
	definir V_valImp Como Real
	definir  V_sueBas Como Real
	definir V_suePag Como Real
	definir  V_valHorNor Como Real
	
	// area de inicialisacion de variables 
	v_nomEmp = ""
	V_horSemTra = 0
	V_valHor = 0
	V_valHorExt = 0
	V_valImp = 0.0
	V_sueBas = 0.0
	V_suePag = 0.0
	V_valHorNor= 0.0
	
	//Area de entradas 
	escribir "digite nombre del empleado"
	leer v_nomEmp
	escribir "digite las hora trabajadas"
	leer V_horSemTra
	escribir "digite el vlor por hora"
	leer V_valHor
	
	
	
	//area de procesos 
	si V_horSemTra < 35 entonces 
		V_sueBas = V_horSemTra*V_valHor
	sino 
		V_sueBas= 35 * V_valHor + (V_horSemTra-35) + V_valHor * 1.5
	FinSi
	
	si V_sueBas >= 300000 y V_sueBas < 400000
		V_valImp = V_sueBas * 0.20 
		si V_sueBas > 400000
			V_valImp = V_sueBas * 0.30
		FinSi
	FinSi
	V_suePag = V_sueBas - V_valImp
	
	//area de salidas
	escribir "nombre: ",v_nomEmp 
	escribir "horas trabajadas: ", V_horSemTra
	escribir" valor por hora: ", V_valHor
	escribir "sueldo base: ", V_sueBas
	escribir "impuestos: ", V_valImp 
	escribir "suledo total: ",V_suePag
FinAlgoritmo
