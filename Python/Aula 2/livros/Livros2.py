import tkinter as tk
from tkinter import messagebox

# Listas de livros por categoria
Terror = ['IT a coisa', 'Drácula', 'Frankenstein', 'O exorcista', 'O iluminado']
Romance = ['A culpa é das estrelas', 'Orgulho e preconceito', 'Para todos os garotos que já amei', 'Dom Casmurro']
FiccaoSci = ['Duna', 'Eu, Robô', 'Fahrenheit 451', 'Bladerunner', 'Jogos Vorazes']
Biografia = ['A cabeça de Steve Jobs', 'Sonho grande', 'A loja de Tudo: Jeff Bezos e era da Amazon', 'Nelson Mandela - Longa Caminhada até a Liberdade']
Fantasia = ['O hobbit', 'Senhor dos anéis', 'Harry Potter: O cálice de fogo', 'Game of Thrones']
Drama = ['O grande Gatsby', 'À espera de um milagre', 'A metamorfose']

# Dicionário para associar categorias às listas de livros
livros = {
    "terror": Terror,
    "romance": Romance,
    "ficção científica": FiccaoSci,
    "biografia": Biografia,
    "fantasia": Fantasia,
    "drama": Drama
}

# Função de busca de livros
def buscar_livros():
    categoria = entrada_categoria.get().lower().strip()
    if categoria in livros:
        resultado = "\n".join(livros[categoria])
        resultado_text.set(f"Livros na categoria '{categoria.capitalize()}':\n\n{resultado}")
    else:
        messagebox.showerror("Erro", f"Não há resultados para '{categoria}'. Por favor, tente uma categoria válida.")

# janela principal
janela = tk.Tk()
janela.title("Busca de Livros por Categoria")
janela.geometry("400x400")
janela.resizable(False, False)

# Variável para exibir o resultado
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
