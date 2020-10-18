package projeto_biblioteca;

import java.util.ArrayList;

public class Item {
    protected int codigo;
    protected boolean status;
    protected ArrayList<Item> itens = new ArrayList<Item>();
    
    public Item() {
    }

    public Item(int codigo, boolean status) {
        this.codigo = codigo;
        this.status = status;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }
}
