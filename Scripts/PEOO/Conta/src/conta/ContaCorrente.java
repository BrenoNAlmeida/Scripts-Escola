package conta;

public class ContaCorrente extends Conta {

    protected float limite;

    public ContaCorrente(String nome, int numeroConta, float limite) {
        super(nome, numeroConta);
        this.limite = limite;
    }

    public ContaCorrente() {
    }

    @Override
    public void saque(float saque) throws SaqueNaoRealizado {
        if (saque < saldo) {
            saldo -= saque;
        } else if (limite > saque) {
            saldo -= saque;
            limite += saldo;
            saldo = 0;
        } else {
            throw new SaqueNaoRealizado();
        }
    }

    @Override
    public void transferencia(float transferencia, Conta c) throws TransferenciaNaoRealizada {
        if (this.saldo > transferencia) {
            saldo -= transferencia;
            c.saldo += transferencia;
        } else if (saldo < transferencia && saldo + limite > transferencia) {
            saldo -= transferencia;
            limite += saldo;
            saldo = 0;
            c.saldo += transferencia;
        } else {
            throw new TransferenciaNaoRealizada();
        }

    }

    @Override
    public String Consultar_usuario() {
        String nome = "nome = " + this.nome;
        String numero_conta = "numero da conta = " + this.numeroConta;
        String limite = "limite = " + this.limite;
        return nome + numero_conta + limite;

    }

}
