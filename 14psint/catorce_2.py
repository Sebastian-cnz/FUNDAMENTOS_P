# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Preguntar qué día de la semana fue el día 1 del mes actual y calcular que día de la semana es hoy. 
	# version:2.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	diadelmes = int()
	primerdia = int()
	dias = str()
	primerdiadelmes = str()
	# area de inicialisacion de variables 
	diadelmes = 0
	primerdia = 0
	dias = ""
	primerdiadelmes = ""
	# Area de entradas 
	dias = [str() for ind0 in range(8)]
	dias[1] = "lunes"
	dias[2] = "martes"
	dias[3] = "miercoles"
	dias[4] = "jueves"
	dias[5] = "viernes"
	dias[6] = "sabado"
	dias[7] = "domingo"
	print("Ingrese el primer dia del mes: (lunes, martes, miercoles, jueves, viernes, sabado, domingo)")
	primerdiadelmes = input()
	print("Ingrese que dia del mes quiere saber")
	diadelmes = int(input())
	# area de procesos 
	if (primerdiadelmes=="lunes"):
		primerdia = 0
	else:
		if (primerdiadelmes=="martes"):
			primerdia = 1
		else:
			if (primerdiadelmes=="miercoles"):
				primerdia = 2
			else:
				if (primerdiadelmes=="jueves"):
					primerdia = 3
				else:
					if (primerdiadelmes=="viernes"):
						primerdia = 4
					else:
						if (primerdiadelmes=="sabado"):
							primerdia = 5
						else:
							primerdia = 6
	# area de salidas
	print((dias[(((diadelmes+primerdia)%7)+1)-1]))

