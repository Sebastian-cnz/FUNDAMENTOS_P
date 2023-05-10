/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SEIS.java."

import java.io.*;

public class seis {

	public static void main(String args[]) {
		int n;
		int r;
		// Area de  documentacion
		// enunciado: Calcular la suma de los cincuenta primeros números enteros. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// proseso
		// salida 
		// area de inicialisacion de variables 
		r = 0;
		// Area de entradas 
		// area de procesos 
		for (n=1;n<=50;n++) {
			r = r+n;
		}
		// area de salidas
		System.out.println(r+" es la suma de los primeros 50 enteros positivos");
	}


}

