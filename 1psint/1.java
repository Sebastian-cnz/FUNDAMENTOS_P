/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "UNO.java."

import java.io.*;

public class uno {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double h;
		double im;
		double sb;
		double sn;
		double v;
		// Area de  documentacion
		// enunciado: Calcular el salario bruto y el salario neto de un trabajador "por horas" conociendo el nombre, número de horas trabajadas, impuestos a pagar y salario neto. 
		// version:1.0  fecha 25/02/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// entrada 
		// entrada 
		// entrada 
		// salida 
		// salida
		// area de inicialisacion de variables 
		h = 0.0;
		v = 0.0;
		im = 0.0;
		sb = 0.0;
		sn = 0.0;
		// Area de entradas 
		System.out.println(" escriba las horas trabajadas");
		h = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" escriba el valor por hora ");
		v = Double.parseDouble(bufEntrada.readLine());
		System.out.println(" escriba el valor de los impuestos");
		im = Double.parseDouble(bufEntrada.readLine());
		// area de procesos 
		sb = h*v;
		sn = sb-im;
		// area de salidas
		System.out.println(" Su salario bruto es"+sb);
		System.out.println(" Su salario neto es"+sn);
	}


}

