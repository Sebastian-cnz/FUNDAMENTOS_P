# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Escribir un algoritmo que acepte tres números enteros e imprima el mayor de ellos. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	n1 = float()
	# entrada 
	n2 = float()
	# entrada 
	n3 = float()
	# salida 
	p = float()
	# area de inicialisacion de variables 
	n1 = 0.0
	n2 = 0.0
	n3 = 0.0
	p = 0.0
	# Area de entradas 
	print("digite el primer numero")
	n1 = float(input())
	print("digite el segundo numero")
	n2 = float(input())
	print("digite el tercer numero")
	n3 = float(input())
	# area de procesos 
	if n1>n2:
		if n1>n3:
			p = n1
		else:
			p = n3
	if n2>n3:
		if n2>n1:
			p = n2
		else:
			p = n1
	if n3>n1:
		if n3>n2:
			p = n3
		else:
			p = n2
	if n1==n2 and n2==n3:
		# area de salidas
		print("los numeros son iguales")
	else:
		# area de salidas
		print(p," es el numero mayor")

