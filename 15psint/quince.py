# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: DDiseñar un programa que lea tres números A, B, C y visualice en pantalla el valor del más grande. Se supone que los tres valores son diferentes. 
	# version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	a = float()
	# entrada 
	b = float()
	# entrada 
	c = float()
	# salida 
	r = float()
	# area de inicialisacion de variables 
	a = 0.0
	b = 0.0
	c = 0.0
	r = 0.0
	# Area de entradas 
	print("digite el primer numero")
	a = float(input())
	print("digite el segundo numero")
	b = float(input())
	print("digite el tercer numero")
	c = float(input())
	# area de procesos 
	if a>b:
		if a>c:
			p = a
		else:
			r = c
	if b>c:
		if b>a:
			p = b
		else:
			r = a
	if c>a:
		if c>b:
			p = c
		else:
			r = b
	if a==b or b==c or c==a:
		# area de salidas
		print("error los numero tienen que se diferentes ")
	else:
		# area de salidas
		print(r," es el numero mayor")

