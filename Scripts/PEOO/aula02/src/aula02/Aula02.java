
package aula02;


public class Aula02 {

   
    public static void main(String[] args) {
          Caneta c1 = new Caneta();  
          c1.modelo = "bic";
          c1.cor = "azul";
          //c1.pontaa = 0.9f;
          c1.carga = 80;
          c1.tampada = false;
          c1.status();
          c1.rabiscar();
    }
    
}