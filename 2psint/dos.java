/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "DOS.java."

import java.io.*;

public class dos {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double c;
		double n;
		double p;
		double r;
		double t;
		// Area de  documentacion
		// enunciado: Calcular la media de una serie de números positivos, suponiendo que los datos se leen desde un terminal. Un valor de cero ?como entrada? indicará que se ha alcanzado el final de la serie de números positivos. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// proceso 
		// proceso 
		// salida
		// area de inicialisacion de variables 
		n = 0.0;
		r = 0.0;
		t = 0.0;
		// Area de entradas 
		System.out.println("ingrese los numeros positivos a los que quiera sacar la media, para finalizar ingrese 0");
		n = Double.parseDouble(bufEntrada.readLine());
		if (n>0) {
			while (n>0) {
				t = n+t;
				System.out.println("ingrese un numero positivo");
				n = Double.parseDouble(bufEntrada.readLine());
				c = c+1;
			}
			// area de procesos 
			r = t/c;
			// area de salidas
			System.out.println("el promedio de los numeros ingresados es "+r);
		} else {
			System.out.println("solo se admiten numeros positivos");
		}
	}


}

