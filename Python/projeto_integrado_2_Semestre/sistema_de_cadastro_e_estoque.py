import tkinter as tk
from tkinter import ttk, messagebox

# Estruturas de dados
class Produto:
    def __init__(self, id, nome, categoria, quantidade):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade

class Movimentacao:
    def __init__(self, tipo, produto_id, quantidade):
        self.tipo = tipo  # 'Se é Entrada' ou 'Saída'
        self.produto_id = produto_id
        self.quantidade = quantidade

# Banco de dados fictício
produtos = {}
movimentacoes = []

# Funções de cadastro
def cadastrar_produto(id, nome, categoria, quantidade):
    if id in produtos:
        return False
    produtos[id] = Produto(id, nome, categoria, quantidade)
    return True

# Funções de movimentação
def movimentar_produto(tipo, produto_id, quantidade):
    if produto_id not in produtos:
        return False
    produto = produtos[produto_id]
    if tipo == 'Saída' and produto.quantidade < quantidade:
        return False
    produto.quantidade += quantidade if tipo == 'Entrada' else -quantidade
    movimentacoes.append(Movimentacao(tipo, produto_id, quantidade))
    return True

# Função para exibir produtos
def gerar_relatorio():
    return [(p.id, p.nome, p.categoria, p.quantidade) for p in produtos.values()]

# Interface gráfica
class EstoqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Estoque")

        # Cadastro de produtos
        ttk.Label(root, text="Cadastro de Produtos").grid(row=0, column=0, columnspan=4, pady=5)
        ttk.Label(root, text="ID").grid(row=1, column=0)
        ttk.Label(root, text="Nome").grid(row=1, column=1)
        ttk.Label(root, text="Categoria").grid(row=1, column=2)
        ttk.Label(root, text="Quantidade").grid(row=1, column=3)
        
        self.id_entry = ttk.Entry(root)
        self.nome_entry = ttk.Entry(root)
        self.categoria_entry = ttk.Entry(root)
        self.quantidade_entry = ttk.Entry(root)

        self.id_entry.grid(row=2, column=0)
        self.nome_entry.grid(row=2, column=1)
        self.categoria_entry.grid(row=2, column=2)
        self.quantidade_entry.grid(row=2, column=3)

        ttk.Button(root, text="Cadastrar Produto", command=self.cadastrar_produto).grid(row=3, column=0, columnspan=4, pady=5)

        # Movimentação
        ttk.Label(root, text="Movimentação de Estoque").grid(row=4, column=0, columnspan=4, pady=5)
        ttk.Label(root, text="ID do Produto").grid(row=5, column=0)
        ttk.Label(root, text="Tipo").grid(row=5, column=1)
        ttk.Label(root, text="Quantidade").grid(row=5, column=2)

        self.mov_id_entry = ttk.Entry(root)
        self.tipo_combobox = ttk.Combobox(root, values=["Entrada", "Saída"])
        self.mov_quantidade_entry = ttk.Entry(root)

        self.mov_id_entry.grid(row=6, column=0)
        self.tipo_combobox.grid(row=6, column=1)
        self.mov_quantidade_entry.grid(row=6, column=2)

        ttk.Button(root, text="Registrar Movimentação", command=self.registrar_movimentacao).grid(row=7, column=0, columnspan=4, pady=5)

        # Relatórios
        ttk.Button(root, text="Gerar Relatório", command=self.gerar_relatorio).grid(row=8, column=0, columnspan=4, pady=5)
        self.relatorio_text = tk.Text(root, width=80, height=15)
        self.relatorio_text.grid(row=9, column=0, columnspan=4, pady=5)

    def cadastrar_produto(self):
        id = self.id_entry.get()
        nome = self.nome_entry.get()
        categoria = self.categoria_entry.get()
        try:
            quantidade = int(self.quantidade_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número!")
            return
        
        if cadastrar_produto(id, nome, categoria, quantidade):
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            self.id_entry.delete(0, tk.END)
            self.nome_entry.delete(0, tk.END)
            self.categoria_entry.delete(0, tk.END)
            self.quantidade_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "ID já cadastrado!")

    def registrar_movimentacao(self):
        produto_id = self.mov_id_entry.get()
        tipo = self.tipo_combobox.get()
        try:
            quantidade = int(self.mov_quantidade_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número!")
            return
        
        if movimentar_produto(tipo, produto_id, quantidade):
            messagebox.showinfo("Sucesso", "Movimentação registrada com sucesso!")
            self.mov_id_entry.delete(0, tk.END)
            self.tipo_combobox.set("")
            self.mov_quantidade_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Erro na movimentação! Verifique o ID e quantidade disponível.")

    def gerar_relatorio(self):
        self.relatorio_text.delete("1.0", tk.END)
        for id, nome, categoria, quantidade in gerar_relatorio():
            self.relatorio_text.insert(tk.END, f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {quantidade}\n")

# Inicialização do app
if __name__ == "__main__":
    root = tk.Tk()
    app = EstoqueApp(root)
    root.mainloop()
