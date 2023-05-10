/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "NUEVE.java."

import java.io.*;

public class nueve {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double n1;
		double n2;
		double n3;
		double p;
		// Area de  documentacion
		// enunciado: Escribir un algoritmo que acepte tres números enteros e imprima el mayor de ellos. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// entrada 
		// entrada 
		// salida 
		// area de inicialisacion de variables 
		n1 = 0.0;
		n2 = 0.0;
		n3 = 0.0;
		p = 0.0;
		// Area de entradas 
		System.out.println("digite el primer numero");
		n1 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite el segundo numero");
		n2 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite el tercer numero");
		n3 = Double.parseDouble(bufEntrada.readLine());
		// area de procesos 
		if (n1>n2) {
			if (n1>n3) {
				p = n1;
			} else {
				p = n3;
			}
		}
		if (n2>n3) {
			if (n2>n1) {
				p = n2;
			} else {
				p = n1;
			}
		}
		if (n3>n1) {
			if (n3>n2) {
				p = n3;
			} else {
				p = n2;
			}
		}
		if (n1==n2 && n2==n3) {
			// area de salidas
			System.out.println("los numeros son iguales");
		} else {
			// area de salidas
			System.out.println(p+" es el numero mayor");
		}
	}


}

