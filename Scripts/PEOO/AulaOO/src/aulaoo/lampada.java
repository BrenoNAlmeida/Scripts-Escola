
package aulaoo;


public class lampada {

 
	private boolean ligada;
	private double potencia;
	
	public void ligar() {
		ligada = true;
	}
	public void desligar() {
		ligada = false;
	}
	public boolean estaLigada() {
		return ligada;
	}
	public double getPotencia() {
		return potencia;
	}
	public void setPotencia(double pot) {
		potencia = pot;
	}

}

