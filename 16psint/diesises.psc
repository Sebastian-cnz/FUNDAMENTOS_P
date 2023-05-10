Algoritmo diesises
	//Area de  documentacion
	//enunciado: Programa que nos permita calcular las soluciones de una ecuación de segundo grado, incluyendo los valores imaginarios
	//version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	
	//Area de definicion de variables
	Definir C como real //entrada 
	Definir B como real //entrada
	definir A como real //entrada
	Definir D como real // salida
	Definir RZ como real // proceso 
	Definir RZ2 como real // proceso 
	
	// area de inicialisacion de variables 
	C = 0.0 
	B = 0.0 
	A = 0.0
	D = 0.0
	RZ = 0.0
	RZ2 = 0.0
	
	//Area de entradas 
	escribir "digite A de la ecuacion"
	leer A
	Mientras A=0 Hacer
		escribir 'A no puede ser 0, ingrese nuevamente'
		leer A
	FinMientras
	
	escribir "digite B de la ecuacion"
	leer B
	escribir "digite C de la ecuacion"
	leer C
	
	
	//area de procesos 
	D = (B^2) - (4 + A + C)
	
	Si D=0 Entonces
		Escribir "La solución de la ecuación es " D;
	SiNo
		Si D>=0 Entonces
			RZ<-(raiz(D))
			RZ2<-(-(raiz(D)))
			escribir '* Raiz positiva: ',Redon(RZ*100)/100 ,', Raiz negativa: ',Redon(RZ2*100)/100
			x1<-((-B)+(RZ))/(2*A) 
			x2<-((-B)+(RZ2))/(2*A)
			Escribir 'Respuesta: x1=',Redon(x1*100)/100,' y x2=',Redon(x2*100)/100
			
		sino
			
			escribir 'La ecuación no tiene soluciones reales (tiene dos soluciones complejas distintas)'
			
			escribir 'x1=i y x2=-i'
			
		FinSi
		
	Fin Si
	//area de salidas
	escribir "el discriminate es" D;
FinAlgoritmo
