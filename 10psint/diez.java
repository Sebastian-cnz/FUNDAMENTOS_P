/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "DIEZ.java."

import java.io.*;

public class diez {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double a;
		double b;
		double x;
		// Area de  documentacion
		// enunciado: Resolución de una ecuación de primer grado. 
		// version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada
		// entrada
		// salida
		// area de inicialisacion de variables 
		b = 0.0;
		a = 0.0;
		x = 0.0;
		// Area de entradas 
		System.out.println("digite A de la ecuacion");
		a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite B de la ecuacion");
		b = Double.parseDouble(bufEntrada.readLine());
		// area de procesos 
		x = (-b)/a;
		// area de salidas
		System.out.println("la ecuacion resulta en "+x);
	}


}

