package contabancaria;

public class Corrente implements ICorrente {

    private String nome;
    private int numero;
    private float saldo;

    public Corrente(String nome, int numero) {
        this.nome = nome;
        this.numero = numero;
    }

    public Corrente() {
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public String getNome() {
        return nome;
    }

    public int getNumero() {
        return numero;
    }

    public float getSaldo() {
        return saldo;
    }

    public Corrente(float saldo) {
        this.saldo = saldo;
    }

    @Override
    public float getextrato() {
        return saldo;
    }

    @Override
    public String setsacar(float valor) {
        if (valor < this.saldo) {
            saldo = saldo - valor;
            return "saque realizado com sucesso";
        } else {
            return "saldo insulficiente";
        }
    }

    @Override
    public void setdeposito(float deposito) {
        saldo = saldo + deposito;
    }

    @Override
    public String getconsultar() {
        return "o usuario é " + this.nome + "\n e o numero da conta é " + this.numero;

    }
}
