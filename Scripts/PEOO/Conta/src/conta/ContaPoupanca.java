package conta;

public class ContaPoupanca extends Conta {

    public void bonus() {
        float bonus = (float) ((saldo * 0.15) / 100);
        saldo += bonus;
    }

    public ContaPoupanca(String nome, int numeroConta) {
        super(nome, numeroConta);
    }

}
