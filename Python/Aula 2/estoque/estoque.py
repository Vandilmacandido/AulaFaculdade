import tkinter as tk
from tkinter import messagebox, ttk
import json

# Arquivo para armazenar os dados do estoque
STOCK_FILE = "estoque.json"

def carregar_estoque():
    try:
        with open(STOCK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_estoque(estoque):
    with open(STOCK_FILE, "w") as f:
        json.dump(estoque, f, indent=4)

def adicionar_produto():
    produto_id = entry_id.get()
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    categoria = entry_categoria.get()

    if not (produto_id and nome and quantidade.isdigit() and categoria):
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return

    quantidade = int(quantidade)
    estoque = carregar_estoque()

    if produto_id in estoque:
        estoque[produto_id]["quantidade"] += quantidade
    else:
        estoque[produto_id] = {"nome": nome, "quantidade": quantidade, "categoria": categoria}

    salvar_estoque(estoque)
    atualizar_tabela()
    limpar_campos()
    messagebox.showinfo("Sucesso", "Produto adicionado/atualizado com sucesso.")

def remover_produto():
    produto_id = entry_id.get()

    if not produto_id:
        messagebox.showerror("Erro", "Informe o ID do produto a ser removido.")
        return

    estoque = carregar_estoque()

    if produto_id in estoque:
        del estoque[produto_id]
        salvar_estoque(estoque)
        atualizar_tabela()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Produto removido com sucesso.")
    else:
        messagebox.showerror("Erro", "Produto não encontrado no estoque.")

def atualizar_tabela():
    for row in tabela.get_children():
        tabela.delete(row)

    estoque = carregar_estoque()
    for produto_id, dados in estoque.items():
        tabela.insert("", tk.END, values=(produto_id, dados["nome"], dados["quantidade"], dados["categoria"]))

def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Sistema de Estoque")

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Campos de entrada
lbl_id = tk.Label(frame, text="ID do Produto:")
lbl_id.grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1, padx=5, pady=5)

lbl_nome = tk.Label(frame, text="Nome do Produto:")
lbl_nome.grid(row=1, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

lbl_quantidade = tk.Label(frame, text="Quantidade:")
lbl_quantidade.grid(row=2, column=0, padx=5, pady=5)
entry_quantidade = tk.Entry(frame)
entry_quantidade.grid(row=2, column=1, padx=5, pady=5)

lbl_categoria = tk.Label(frame, text="Categoria:")
lbl_categoria.grid(row=3, column=0, padx=5, pady=5)
entry_categoria = tk.Entry(frame)
entry_categoria.grid(row=3, column=1, padx=5, pady=5)

# Botões
btn_adicionar = tk.Button(frame, text="Adicionar/Atualizar", command=adicionar_produto)
btn_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

btn_remover = tk.Button(frame, text="Remover", command=remover_produto)
btn_remover.grid(row=5, column=0, columnspan=2, pady=5)

# Tabela para exibir o estoque
tabela_frame = tk.Frame(root)
tabela_frame.pack(pady=10, padx=10)

colunas = ("ID", "Nome", "Quantidade", "Categoria")
tabela = ttk.Treeview(tabela_frame, columns=colunas, show="headings")

for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=100)

tabela.pack()

atualizar_tabela()

root.mainloop()
