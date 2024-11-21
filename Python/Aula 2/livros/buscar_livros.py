import tkinter as tk
from tkinter import messagebox

# Dicionário com categorias de livros e suas opções
livros = {
    "romance": [
        "Orgulho e Preconceito - Jane Austen",
        "Como Eu Era Antes de Você - Jojo Moyes",
        "O Morro dos Ventos Uivantes - Emily Brontë"
    ],
    "terror": [
        "It: A Coisa - Stephen King",
        "O Exorcista - William Peter Blatty",
        "Drácula - Bram Stoker"
    ],
    "ficcao_cientifica": [
        "Duna - Frank Herbert",
        "Neuromancer - William Gibson",
        "Fahrenheit 451 - Ray Bradbury"
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
    categoria = entrada_categoria.get().lower().strip()
    if categoria in livros:
        # Exibe os livros da categoria escolhida
        resultado = "\n".join(livros[categoria])
        resultado_text.set(f"Livros na categoria '{categoria.capitalize()}':\n\n{resultado}")
    else:
        messagebox.showerror("Erro", "Categoria não encontrada. Por favor, tente uma categoria válida.")

# Configurações da janela principal
janela = tk.Tk()
janela.title("Busca de Livros por Categoria")
janela.geometry("400x400")
janela.resizable(False, False)

# Variáveis para a interface
resultado_text = tk.StringVar()

# Título
titulo_label = tk.Label(janela, text="Busque Livros por Categoria", font=("Arial", 14, "bold"))
titulo_label.pack(pady=10)

# Campo de entrada para digitar a categoria
categoria_label = tk.Label(janela, text="Digite a categoria desejada:", font=("Arial", 10))
categoria_label.pack(pady=5)

entrada_categoria = tk.Entry(janela, font=("Arial", 10))
entrada_categoria.pack(pady=5)

# Botão de busca
buscar_button = tk.Button(janela, text="Buscar", command=buscar_livros)
buscar_button.pack(pady=10)

# Resultado da busca
resultado_label = tk.Label(janela, textvariable=resultado_text, wraplength=350, justify="left", font=("Arial", 10))
resultado_label.pack(pady=10)

# Inicia a interface
janela.mainloop()
