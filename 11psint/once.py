# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Area de  documentacion
	# enunciado: Se desea obtener la nómina semana, salario neto? de los empleados de una empresa cuyo trabajo se paga por horas
	# version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
	# Area de definicion de variables
	v_nomemp = str()
	v_horsemtra = int()
	v_valhor = int()
	v_valhorext = int()
	v_valimp = float()
	v_suebas = float()
	v_suepag = float()
	v_valhornor = float()
	# area de inicialisacion de variables 
	v_nomemp = ""
	v_horsemtra = 0
	v_valhor = 0
	v_valhorext = 0
	v_valimp = 0.0
	v_suebas = 0.0
	v_suepag = 0.0
	v_valhornor = 0.0
	# Area de entradas 
	print("digite nombre del empleado")
	v_nomemp = input()
	print("digite las hora trabajadas")
	v_horsemtra = int(input())
	print("digite el vlor por hora")
	v_valhor = int(input())
	# area de procesos 
	if v_horsemtra<35:
		v_suebas = v_horsemtra*v_valhor
	else:
		v_suebas = 35*v_valhor+(v_horsemtra-35)+v_valhor*1.5
	if v_suebas>=300000 and v_suebas<400000:
		v_valimp = v_suebas*0.20
		if v_suebas>400000:
			v_valimp = v_suebas*0.30
	v_suepag = v_suebas-v_valimp
	# area de salidas
	print("nombre: ",v_nomemp)
	print("horas trabajadas: ",v_horsemtra)
	print(" valor por hora: ",v_valhor)
	print("sueldo base: ",v_suebas)
	print("impuestos: ",v_valimp)
	print("suledo total: ",v_suepag)

