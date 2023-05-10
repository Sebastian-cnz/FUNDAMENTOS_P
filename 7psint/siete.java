/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SIETE.java."

import java.io.*;

public class siete {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int n;
		int p;
		int r;
		// Area de  documentacion
		// enunciado: Escribir un algoritmo que calcule el producto de los n primeros números naturales. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// proceso 
		// salida 
		// area de inicialisacion de variables 
		r = 0;
		n = 0;
		// Area de entradas 
		System.out.println("ingrese la cantidad de naturales a sumar");
		n = Integer.parseInt(bufEntrada.readLine());
		// area de procesos 
		for (p=1;p<=n;p++) {
			r = r+p;
		}
		// area de salidas
		System.out.println(r+" es el producto de los primeros "+n+" numeros naturales");
	}


}

