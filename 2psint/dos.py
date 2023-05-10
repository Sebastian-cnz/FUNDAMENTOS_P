# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Calcular la media de una serie de números positivos, suponiendo que los datos se leen desde un terminal. Un valor de cero ?como entrada? indicará que se ha alcanzado el final de la serie de números positivos. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	n = float()
	# proceso 
	c = float()
	# proceso 
	t = float()
	# salida
	p = float()
	# area de inicialisacion de variables 
	n = 0.0
	r = 0.0
	t = 0.0
	# Area de entradas 
	print("ingrese los numeros positivos a los que quiera sacar la media, para finalizar ingrese 0")
	n = float(input())
	if n>0:
		while n>0:
			t = n+t
			print("ingrese un numero positivo")
			n = float(input())
			c = c+1
		# area de procesos 
		r = t/c
		# area de salidas
		print("el promedio de los numeros ingresados es ",r)
	else:
		print("solo se admiten numeros positivos")

