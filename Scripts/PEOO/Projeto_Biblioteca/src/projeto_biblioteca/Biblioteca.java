 package projeto_biblioteca;

import java.util.ArrayList;

public class Biblioteca {
    private String nome;
    private String responsavel;
    ArrayList<Livro> livros = new ArrayList<Livro>();

    public Biblioteca(String nome, String responsavel) {
        this.nome = nome;
        this.responsavel = responsavel;
    }

    public Biblioteca() {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getResponsavel() {
        return responsavel;
    }

    public void setResponsavel(String responsavel) {
        this.responsavel = responsavel;
    }

    public ArrayList<Livro> getLivros() {
        return livros;
    }

    public void setLivros(ArrayList<Livro> livros) {
        this.livros = livros;
    }
    
    public void inserirLivro(Livro l){
        livros.add(l);
    }    

    public Livro buscarLivro(String titulo) throws ItemNaoEncotradoException{
        for (Livro l : livros) {
            if(l.getTitulo().equalsIgnoreCase(titulo))
                return l;
        }
        throw new ItemNaoEncotradoException();
    }
    
    public void removerLivro(String titulo) throws ItemNaoEncotradoException{
        Livro l = buscarLivro(titulo);
        livros.remove(l);
    }
    
    public Livro listarLivro(String titulo) throws ItemNaoEncotradoException{
        for (Livro l : livros) {
                return l;
        }
        throw new ItemNaoEncotradoException();
    }
    
}
