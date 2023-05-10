/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "TRECE.java."

import java.io.*;

public class trece {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int f;
		int n;
		// Area de  documentacion
		// enunciado: Leída una fecha, decir el día de la semana, suponiendo que el día 1 de dicho mes fue lunes
		// version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// proceso
		// area de inicialisacion de variables 
		f = 0;
		n = 0;
		// Area de entradas 
		System.out.println("digite la fecha");
		f = Integer.parseInt(bufEntrada.readLine());
		// area de procesos 
		n = f%7;
		// area de salidas
		if (n==1) {
			System.out.println("el dia es lunes ");
		}
		if (n==2) {
			System.out.println("el dia es martes ");
		}
		if (n==3) {
			System.out.println("el dia es miercoles ");
		}
		if (n==4) {
			System.out.println("el dia es jueves ");
		}
		if (n==5) {
			System.out.println("el dia es viernes ");
		}
		if (n==6) {
			System.out.println("el dia es sabado ");
		}
		if (n==7) {
			System.out.println("el dia es domingo ");
		}
	}


}

