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

def buscar_livros_por_categoria(categoria):
    # Verifica se a categoria existe no dicionário
    if categoria in livros:
        print(f"Livros na categoria '{categoria.capitalize()}':")
        for livro in livros[categoria]:
            print(f"- {livro}")
    else:
        print("Categoria não encontrada. Tente uma das seguintes opções:")
        for cat in livros.keys():
            print(f"- {cat.capitalize()}")

# uso
categoria_escolhida = input("Digite a categoria desejada (romance, terror, ficcao_cientifica, fantasia, drama, biografia): ").lower()
buscar_livros_por_categoria(categoria_escolhida)
