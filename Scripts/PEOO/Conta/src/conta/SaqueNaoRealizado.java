
package conta;


public class SaqueNaoRealizado extends Exception {

    public SaqueNaoRealizado() {
        super("imposivel realizar saque, seu Saldo é Insuficiente");
    }
    
}
