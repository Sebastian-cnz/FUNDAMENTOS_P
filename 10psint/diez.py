# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Resolución de una ecuación de primer grado. 
	# version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada
	b = float()
	# entrada
	a = float()
	# salida
	x = float()
	# area de inicialisacion de variables 
	b = 0.0
	a = 0.0
	x = 0.0
	# Area de entradas 
	print("digite A de la ecuacion")
	a = float(input())
	print("digite B de la ecuacion")
	b = float(input())
	# area de procesos 
	x = (-b)/a
	# area de salidas
	print("la ecuacion resulta en ",x)

