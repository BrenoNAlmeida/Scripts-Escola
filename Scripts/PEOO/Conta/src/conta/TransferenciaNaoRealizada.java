
package conta;


public class TransferenciaNaoRealizada extends Exception {

    public TransferenciaNaoRealizada() {
        super("Transferencia não realizada, saldo insuficiente");
    }
    
}
