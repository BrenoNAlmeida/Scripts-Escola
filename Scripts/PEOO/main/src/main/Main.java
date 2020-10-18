
package main;


public class Main {

   
    public static void main(String[] args) {
        agenda ag = new agenda (10);
        Tarefa t = new Tarefa();
        t.assunto = "aula 1";
        ag.tarefas[0]= t ;
        System.out.println(ag.tarefas[0]);
    }
    
}
