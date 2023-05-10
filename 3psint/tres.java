/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "TRES.java."

import java.io.*;

public class tres {

	public static void main(String args[]) {
		int n;
		int s;
		// Area de  documentacion
		// enunciado: Suma de los números pares comprendidos entre 2 y 100. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// proceso 
		// Salida
		// area de inicialisacion de variables 
		s = 0;
		// Area de entradas 
		// area de procesos 
		for (n=2;n<=100;n++) {
			if (n%2==0) {
				s = s+n;
			}
		}
		// area de salidas
		System.out.println("La suma de los números pares es: "+s);
	}


}

