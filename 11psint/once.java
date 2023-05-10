/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "ONCE.java."

import java.io.*;

public class once {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_horsemtra;
		String v_nomemp;
		double v_suebas;
		double v_suepag;
		int v_valhor;
		int v_valhorext;
		double v_valhornor;
		double v_valimp;
		// Area de  documentacion
		// enunciado: Se desea obtener la nómina semana, salario neto? de los empleados de una empresa cuyo trabajo se paga por horas
		// version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// area de inicialisacion de variables 
		v_nomemp = "";
		v_horsemtra = 0;
		v_valhor = 0;
		v_valhorext = 0;
		v_valimp = 0.0;
		v_suebas = 0.0;
		v_suepag = 0.0;
		v_valhornor = 0.0;
		// Area de entradas 
		System.out.println("digite nombre del empleado");
		v_nomemp = bufEntrada.readLine();
		System.out.println("digite las hora trabajadas");
		v_horsemtra = Integer.parseInt(bufEntrada.readLine());
		System.out.println("digite el vlor por hora");
		v_valhor = Integer.parseInt(bufEntrada.readLine());
		// area de procesos 
		if (v_horsemtra<35) {
			v_suebas = v_horsemtra*v_valhor;
		} else {
			v_suebas = 35*v_valhor+(v_horsemtra-35)+v_valhor*1.5;
		}
		if (v_suebas>=300000 && v_suebas<400000) {
			v_valimp = v_suebas*0.20;
			if (v_suebas>400000) {
				v_valimp = v_suebas*0.30;
			}
		}
		v_suepag = v_suebas-v_valimp;
		// area de salidas
		System.out.println("nombre: "+v_nomemp);
		System.out.println("horas trabajadas: "+v_horsemtra);
		System.out.println(" valor por hora: "+v_valhor);
		System.out.println("sueldo base: "+v_suebas);
		System.out.println("impuestos: "+v_valimp);
		System.out.println("suledo total: "+v_suepag);
	}


}

