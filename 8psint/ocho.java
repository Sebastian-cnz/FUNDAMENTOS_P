/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "OCHO.java."

import java.io.*;
import java.math.*;

public class ocho {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double a;
		double b;
		double c;
		double d;
		double rz;
		double rz2;
		double x1;
		double x2;
		// Area de  documentacion
		// enunciado: Diseñar un algoritmo para resolver una ecuación de segundo grado Ax2 + Bx + C = 0. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// entrada
		// entrada
		// salida
		// proceso 
		// proceso 
		// area de inicialisacion de variables 
		c = 0.0;
		b = 0.0;
		a = 0.0;
		d = 0.0;
		rz = 0.0;
		rz2 = 0.0;
		// Area de entradas 
		System.out.println("digite A de la ecuacion");
		a = Double.parseDouble(bufEntrada.readLine());
		while (a==0) {
			System.out.println("A no puede ser 0, ingrese nuevamente");
			a = Double.parseDouble(bufEntrada.readLine());
		}
		System.out.println("digite B de la ecuacion");
		b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("digite C de la ecuacion");
		c = Double.parseDouble(bufEntrada.readLine());
		// area de procesos 
		d = (Math.pow(b,2))-(4+a+c);
		if (d==0) {
			System.out.println("La solución de la ecuación es "+d);
		} else {
			if (d>=0) {
				rz = (Math.sqrt(d));
				rz2 = (-(Math.sqrt(d)));
				System.out.println("* Raiz positiva: "+Math.round(rz*100)/100+"Raiz negativa: "+Math.round(rz2*100)/100);
				x1 = ((-b)+(rz))/(2*a);
				x2 = ((-b)+(rz2))/(2*a);
				System.out.println("Respuesta: x1="+Math.round(x1*100)/100+" y x2="+Math.round(x2*100)/100);
			} else {
				System.out.println("error numero imaginarios");
			}
		}
		// area de salidas
		System.out.println("el discriminate es"+d);
	}


}

