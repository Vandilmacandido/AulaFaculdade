import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário com categorias de livros e suas opções
livros = {
    "romance": [
        "Orgulho e Preconceito - Jane Austen",
        "Como Eu Era Antes de Você - Jojo Moyes",
        "O Morro dos Ventos Uivantes - Emily Brontë"
    ],
    "terror": [
        "It: A Coisa - Stephen King",
        "Drácula - Bram Stoker",
        "Frankenstein - Mary Shelley",
        "O Exorcista - William Peter Blatty",
        "O iluminado - Stephen King"
    ],
    "ficcao_cientifica": [
        "Duna - Frank Herbert",
        "Eu, Robô - Isaac Asimov",
        "Fahrenheit 451 - Ray Bradbury",
        "Bladerunner - Philip K. Dick",
        "Jogos Vorazes - Suzanne Collins"       
    ],
    "fantasia": [
        "O Senhor dos Anéis - J.R.R. Tolkien",
        "Harry Potter e a Pedra Filosofal - J.K. Rowling",
        "O Nome do Vento - Patrick Rothfuss"
    ],
    "drama": [
        "A Menina que Roubava Livros - Markus Zusak",
        "O Sol é para Todos - Harper Lee",
        "Cem Anos de Solidão - Gabriel García Márquez"
    ],
    "biografia": [
        "Steve Jobs - Walter Isaacson",
        "Eu Sou Malala - Malala Yousafzai",
        "Longa Caminhada até a Liberdade - Nelson Mandela"
    ]
}

# Função de busca de livros
def buscar_livros():
    categoria = categoria_var.get().lower()
    if categoria in livros:
        # Exibe os livros da categoria escolhida
        resultado = "\n".join(livros[categoria])
        resultado_text.set(f"Livros na categoria '{categoria.capitalize()}':\n\n{resultado}")
    else:
        messagebox.showerror("Erro", "Categoria não encontrada. Por favor, selecione uma categoria válida.")

# Configurações da janela principal
janela = tk.Tk()
janela.title("Busca de Livros por Categoria")
janela.geometry("400x400")
janela.resizable(False, False)

# Variáveis para a interface
categoria_var = tk.StringVar()
resultado_text = tk.StringVar()

# Título
titulo_label = tk.Label(janela, text="Busque Livros por Categoria", font=("Arial", 14, "bold"))
titulo_label.pack(pady=10)

# Seleção de categoria
categoria_label = tk.Label(janela, text="Selecione uma categoria:", font=("Arial", 10))
categoria_label.pack(pady=5)

categoria_combo = ttk.Combobox(janela, textvariable=categoria_var, state="readonly")
categoria_combo['values'] = list(livros.keys())
categoria_combo.pack()

# Botão de busca
buscar_button = tk.Button(janela, text="Buscar", command=buscar_livros)
buscar_button.pack(pady=10)

# Resultado da busca
resultado_label = tk.Label(janela, textvariable=resultado_text, wraplength=350, justify="left", font=("Arial", 10))
resultado_label.pack(pady=10)

# Inicia a interface
janela.mainloop()
