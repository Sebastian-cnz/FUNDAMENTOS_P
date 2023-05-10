# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, número de horas trabajadas, impuestos a pagar y salario neto. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	h = float()
	# entrada 
	v = float()
	# entrada 
	im = float()
	# salida 
	sb = float()
	# salida
	sn = float()
	# area de inicialisacion de variables 
	h = 0.0
	v = 0.0
	im = 0.0
	sb = 0.0
	sn = 0.0
	# Area de entradas 
	print(" escriba las horas trabajadas")
	h = float(input())
	print(" escriba el valor por hora ")
	v = float(input())
	print(" escriba el valor de los impuestos")
	im = float(input())
	# area de procesos 
	sb = h*v
	sn = sb-im
	# area de salidas
	print(" Su salario bruto es",sb)
	print(" Su salario neto es",sn)

