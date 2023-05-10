# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Area de  documentacion
	# enunciado:Programa que nos calcule el área de un triángulo conociendo sus lados. 
	# version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	l1 = float()
	# entrada 
	l2 = float()
	# entrada 
	l3 = float()
	# proceso
	sp = float()
	# salida 
	a = float()
	# area de inicialisacion de variables 
	l1 = 0.0
	l2 = 0.0
	l3 = 0.0
	a = 0.0
	sp = 0.0
	# Area de entradas
	print("digite el lado 1")
	l1 = float(input())
	print("digite el lado 2")
	l2 = float(input())
	print("digite el lado 3")
	l3 = float(input())
	# area de procesos 
	sp = (l1+l2+l3)/2
	a = sqrt(sp*(sp-l1)*(sp-l2)*(sp-l3))
	# area de salidas
	print("el area es igual a ",a)

