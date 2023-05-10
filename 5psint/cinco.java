/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "CINCO.java."

import java.io.*;

public class cinco {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double c;
		double m;
		double p;
		double r;
		// Area de  documentacion
		// enunciado: Determinar la cantidad total a pagar por una llamada telefónica, teniendo en cuenta lo siguiente: toda llamada que dure menos de tres minutos (cinco pasos) tiene un coste de 10 céntimos, cada minuto adicional a partir de los tres primeros es un paso de contador y cuesta 5 céntimos. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// salida 
		// constante 5
		// proseso 
		// area de inicialisacion de variables 
		m = 0.0;
		r = 0.0;
		c = 5;
		p = 0.0;
		// Area de entradas 
		System.out.println("digite los mituos de la llamada");
		m = Double.parseDouble(bufEntrada.readLine());
		// area de procesos 
		if (m>3) {
			p = m-3;
			r = p*5+10;
		} else {
			r = 10;
		}
		// area de salidas
		System.out.println("el valor de la llamada son "+r+" centimos");
	}


}

