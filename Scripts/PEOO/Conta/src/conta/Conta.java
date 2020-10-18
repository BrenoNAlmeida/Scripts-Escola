package conta;

public class Conta {

    protected String nome;
    protected int numeroConta;
    protected float saldo;

    public Conta(String nome, int numeroConta) {
        this.nome = nome;
        this.numeroConta = numeroConta;
    }

    public Conta() {
    }

    public String getNome() {
        return nome;
    }

    public int getNumeroConta() {
        return numeroConta;
    }

    public float getSaldo() {
        return saldo;
    }

    public float deposito(float deposito) {
        saldo += deposito;
        return saldo;
    }

    public String Consultar_usuario() {
        String nome = "nome = " + getNome();
        String numero_conta = "numero da conta = " + getNumeroConta();
        return nome + numero_conta;

    }

    public void saque(float saque) throws SaqueNaoRealizado {
        if (saque > saldo) {
            saldo -= saque;
        } else {
            throw new SaqueNaoRealizado();
        }
    }

    public void transferencia(float transferencia, Conta c) throws TransferenciaNaoRealizada {
        if (this.saldo > transferencia) {
            saldo -= transferencia;
            c.saldo += transferencia;
        } else {
            throw new TransferenciaNaoRealizada();
        }

    }

}
