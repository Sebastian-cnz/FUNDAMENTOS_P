/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "QUINCE.java."

import java.io.*;

public class quince {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double a;
		double b;
		double c;
		double p;
		double r;
		// Area de  documentacion
		// enunciado: DDiseñar un programa que lea tres números A, B, C y visualice en pantalla el valor del más grande. Se supone que los tres valores son diferentes. 
		// version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// entrada 
		// entrada 
		// salida 
		// area de inicialisacion de variables 
		a = 0.0;
		b = 0.0;
		c = 0.0;
		r = 0.0;
		// Area de entradas 
		System.out.println("digite el primer numero");
		a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite el segundo numero");
		b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite el tercer numero");
		c = Double.parseDouble(bufEntrada.readLine());
		// area de procesos 
		if (a>b) {
			if (a>c) {
				p = a;
			} else {
				r = c;
			}
		}
		if (b>c) {
			if (b>a) {
				p = b;
			} else {
				r = a;
			}
		}
		if (c>a) {
			if (c>b) {
				p = c;
			} else {
				r = b;
			}
		}
		if (a==b || b==c || c==a) {
			// area de salidas
			System.out.println("error los numero tienen que se diferentes ");
		} else {
			// area de salidas
			System.out.println(r+" es el numero mayor");
		}
	}


}

