package projeto_biblioteca;

import java.util.ArrayList;

public class Livro {
    protected String titulo;
    protected String autor;
    protected int ano;
    protected String tipo;
    
    protected ArrayList<Item> itens = new ArrayList<Item>();

    public Livro(String titulo, String autor, int ano, String tipo) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.tipo = tipo;
    }

    public Livro() {
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public void inserirItem(Item i){
        itens.add(i);
    }    

    public Item buscarItem(int cod) throws ItemNaoEncotradoException{
        for (Item i : itens) {
            if(i.getCodigo() == cod)
                return i;
        }
        throw new ItemNaoEncotradoException();
    }
    public void removerItem(int cod) throws ItemNaoEncotradoException{
        Item i = buscarItem(cod);
        itens.remove(i);
    }
}
