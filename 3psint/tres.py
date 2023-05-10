# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Suma de los números pares comprendidos entre 2 y 100. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# proceso 
	n = int()
	# Salida
	s = int()
	# area de inicialisacion de variables 
	s = 0
	# Area de entradas 
	# area de procesos 
	for n in range(2,101):
		if n%2==0:
			s = s+n
	# area de salidas
	print("La suma de los números pares es: ",s)

