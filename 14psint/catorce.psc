Algoritmo catorce
	//Area de  documentacion
	//enunciado: Preguntar qué día de la semana fue el día 1 del mes actual y calcular que día de la semana es hoy. 
	//version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	definir dia Como caracter
	definir fecha como entero 
	// area de inicialisacion de variables 
	dia = ""
	jueves = ""
	viernes = ""
	sabado = ""
	domingo = ""
	miercoles = ""
	martes = ""
	fecha =0 
	//Area de entradas 
	escribir "que dia de la semana fue el dia 1 del mes"
	leer dia
	mientras dia <> "lunes" o "martes" o "miercoles" jueves, vienrnes, sabado, domingo 
		escribir "dia no valido porfavor dijite un dia real"
		leer dia 
	FinMientras
	escribir " indique  la fecha actual"
	leer fecha
	
	
	//area de procesos 
	
	si dia = lunes entonces 
		N = fecha mod 7
	FinSi
	si dia = lunes entonces 
		N = fecha mod 7
	FinSi
	si dia = lunes entonces 
		N = fecha mod 7
	FinSi
	
	escribir N
	
	//primer dia martes, fehca actual 6 
	
	
	//area de salidas
	
	
FinAlgoritmo
