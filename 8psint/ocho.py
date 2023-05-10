# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Diseñar un algoritmo para resolver una ecuación de segundo grado Ax2 + Bx + C = 0. 
	# version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	c = float()
	# entrada
	b = float()
	# entrada
	a = float()
	# salida
	d = float()
	# proceso 
	rz = float()
	# proceso 
	rz2 = float()
	# area de inicialisacion de variables 
	c = 0.0
	b = 0.0
	a = 0.0
	d = 0.0
	rz = 0.0
	rz2 = 0.0
	# Area de entradas 
	print("digite A de la ecuacion")
	a = float(input())
	while a==0:
		print("A no puede ser 0, ingrese nuevamente")
		a = float(input())
	print("digite B de la ecuacion")
	b = float(input())
	print("digite C de la ecuacion")
	c = float(input())
	# area de procesos 
	d = (b**2)-(4+a+c)
	if d==0:
		print("La solución de la ecuación es ",d)
	else:
		if d>=0:
			rz = (sqrt(d))
			rz2 = (-(sqrt(d)))
			print("* Raiz positiva: ",round(rz*100)/100,"Raiz negativa: ",round(rz2*100)/100)
			x1 = ((-b)+(rz))/(2*a)
			x2 = ((-b)+(rz2))/(2*a)
			print("Respuesta: x1=",round(x1*100)/100," y x2=",round(x2*100)/100)
		else:
			print("error numero imaginarios")
	# area de salidas
	print("el discriminate es",d)

