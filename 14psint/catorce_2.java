/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "CATORCE_2.java."

import java.io.*;

public class catorce_2 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int diadelmes;
		String dias[];
		int primerdia;
		String primerdiadelmes;
		// Area de  documentacion
		// enunciado: Preguntar qué día de la semana fue el día 1 del mes actual y calcular que día de la semana es hoy. 
		// version:2.0  fecha 02/03/23 desarrollado:Sebstian Carrilo
		// Area de definicion de variables
		// area de inicialisacion de variables 
		diadelmes = 0;
		primerdia = 0;
		dias = "";
		primerdiadelmes = "";
		// Area de entradas 
		dias = new String[8];
		dias[1] = "lunes";
		dias[2] = "martes";
		dias[3] = "miercoles";
		dias[4] = "jueves";
		dias[5] = "viernes";
		dias[6] = "sabado";
		dias[7] = "domingo";
		System.out.println("Ingrese el primer dia del mes: (lunes, martes, miercoles, jueves, viernes, sabado, domingo)");
		primerdiadelmes = bufEntrada.readLine();
		System.out.println("Ingrese que dia del mes quiere saber");
		diadelmes = Integer.parseInt(bufEntrada.readLine());
		// area de procesos 
		if ((primerdiadelmes.equals("lunes"))) {
			primerdia = 0;
		} else {
			if ((primerdiadelmes.equals("martes"))) {
				primerdia = 1;
			} else {
				if ((primerdiadelmes.equals("miercoles"))) {
					primerdia = 2;
				} else {
					if ((primerdiadelmes.equals("jueves"))) {
						primerdia = 3;
					} else {
						if ((primerdiadelmes.equals("viernes"))) {
							primerdia = 4;
						} else {
							if ((primerdiadelmes.equals("sabado"))) {
								primerdia = 5;
							} else {
								primerdia = 6;
							}
						}
					}
				}
			}
		}
		// area de salidas
		System.out.println((dias[(((diadelmes+primerdia)%7)+1)-1]));
	}


}

