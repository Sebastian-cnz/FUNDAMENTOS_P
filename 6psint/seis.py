# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Calcular la suma de los cincuenta primeros números enteros. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# proseso
	n = int()
	# salida 
	r = int()
	# area de inicialisacion de variables 
	r = 0
	# Area de entradas 
	# area de procesos 
	for n in range(1,51):
		r = r+n
	# area de salidas
	print(r," es la suma de los primeros 50 enteros positivos")

