/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "DOCE.java."

import java.io.*;
import java.math.*;

public class doce {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double a;
		double l1;
		double l2;
		double l3;
		double sp;
		// Area de  documentacion
		// enunciado:Programa que nos calcule el área de un triángulo conociendo sus lados. 
		// version:1.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// entrada 
		// entrada 
		// proceso
		// salida 
		// area de inicialisacion de variables 
		l1 = 0.0;
		l2 = 0.0;
		l3 = 0.0;
		a = 0.0;
		sp = 0.0;
		// Area de entradas
		System.out.println("digite el lado 1");
		l1 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite el lado 2");
		l2 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite el lado 3");
		l3 = Double.parseDouble(bufEntrada.readLine());
		// area de procesos 
		sp = (l1+l2+l3)/2;
		a = Math.sqrt(sp*(sp-l1)*(sp-l2)*(sp-l3));
		// area de salidas
		System.out.println("el area es igual a "+a);
	}


}

