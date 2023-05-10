# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Se desea realizar el algoritmo que resuelva el siguiente problema: Cálculo de los salarios mensuales de los empleados de una empresa, sabiendo que éstos se calculan en base a las horas semanales trabajadas y de acuerdo a un precio especificado por horas. Si se pasan de cuarenta horas semanales, las horas extraordinarias se pagarán a razón de 1,5 veces la hora ordinaria. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# entrada 
	hs = float()
	# entrada 
	v = float()
	# proseso 
	n = float()
	# constante
	a = float()
	# salida 
	s = float()
	# area de inicialisacion de variables 
	hs = 0.0
	v = 0.0
	n = 0.0
	im = 0.0
	a = 1.5
	s = 0.0
	# Area de entradas 
	print(" escriba las horas trabajadas en la semana")
	hs = float(input())
	print(" escriba el valor por horas")
	v = float(input())
	# area de procesos 
	if hs>40:
		n = hs-40
		s = hs*v
		e = n*a
		s = e+s
	else:
		s = hs*v
	# area de salidas
	print(" el salario es",s)

