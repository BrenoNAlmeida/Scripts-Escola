
package calculadora;


public class Racional {
    private int numerador;
    private int denominador;
    public void multiplicar (int numerador, int denominador){
        this.numerador *= numerador;
        this.numerador *= denominador;
        
    }
    public void dividir(int numerador, int denominador){
        this.numerador *= denominador;
        this.denominador *= numerador;
    }
    public void somar (int numerador, int denominador){
        int novod = this.denominador *denominador;
        int n1 = (novod / this.denominador)*this.numerador;
        int n2 = (novod / denominador)*numerador;
        this.numerador = n1 + n2;
        this.denominador = novod;
    }
    public void simplificar (){
    
    }
}
