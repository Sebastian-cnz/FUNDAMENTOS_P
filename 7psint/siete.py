# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Escribir un algoritmo que calcule el producto de los n primeros n�meros naturales. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	n = int()
	# proceso 
	p = int()
	# salida 
	r = int()
	# area de inicialisacion de variables 
	r = 0
	n = 0
	# Area de entradas 
	print("ingrese la cantidad de naturales a sumar")
	n = int(input())
	# area de procesos 
	for p in range(1,n+1):
		r = r+p
	# area de salidas
	print(r," es el producto de los primeros ",n," numeros naturales")

