package aula02;

public class Caneta {

    public String modelo;
    public String cor;
    private float pontaa;
    protected int carga;
    protected boolean tampada;

    public void rabiscar() {
        if (this.tampada == true) {
            System.out.println("a caneta esta tampada, nao posso rabiscar");
        } else {
            System.out.println("estou rabiscando");
        }
    }

    protected void tampar() {
        this.tampada = true;
    }

    protected void destampar() {
        this.tampada = false;
    }

    public void status() {
        System.out.println("uma caneta : " + this.cor);
        System.out.println("esta tampada : " + this.tampada);
        System.out.println("o modelo é : " + this.modelo);
        System.out.println("a ponta é : " + this.pontaa);
        System.out.println("a carga esta em  : " + this.carga);
    }
}
