# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Leída una fecha, decir el día de la semana, suponiendo que el día 1 de dicho mes fue lunes
	# version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	# entrada 
	f = int()
	# proceso
	n = int()
	# area de inicialisacion de variables 
	f = 0
	n = 0
	# Area de entradas 
	print("digite la fecha")
	f = int(input())
	# area de procesos 
	n = f%7
	# area de salidas
	if n==1:
		print("el dia es lunes ")
	if n==2:
		print("el dia es martes ")
	if n==3:
		print("el dia es miercoles ")
	if n==4:
		print("el dia es jueves ")
	if n==5:
		print("el dia es viernes ")
	if n==6:
		print("el dia es sabado ")
	if n==7:
		print("el dia es domingo ")

