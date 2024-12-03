# Estruturas de dados
class Produto:
    def __init__(self, id, nome, categoria, quantidade):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade

class Movimentacao:
    def __init__(self, tipo, produto_id, quantidade):
        self.tipo = tipo  # 'Entrada' ou 'Saída'
        self.produto_id = produto_id
        self.quantidade = quantidade

# Banco de dados fictício
produtos = {}
movimentacoes = []

# Funções de cadastro
def cadastrar_produto(id, nome, categoria, quantidade):
    """
    Cadastra um produto no banco de dados fictício.
    """
    if id in produtos:
        return False  # ID já existe
    produtos[id] = Produto(id, nome, categoria, quantidade)
    return True

# Funções de movimentação
def movimentar_produto(tipo, produto_id, quantidade):
    """
    Registra uma movimentação no estoque (entrada ou saída).
    """
    if produto_id not in produtos:
        return False  # Produto não existe
    produto = produtos[produto_id]
    if tipo == 'Saída' and produto.quantidade < quantidade:
        return False  # Estoque insuficiente para saída
    produto.quantidade += quantidade if tipo == 'Entrada' else -quantidade
    movimentacoes.append(Movimentacao(tipo, produto_id, quantidade))
    return True

# Função para exibir produtos
def gerar_relatorio():
    """
    Gera um relatório com os produtos cadastrados e suas quantidades.
    """
    relatorio = []
    for produto in produtos.values():
        relatorio.append((produto.id, produto.nome, produto.categoria, produto.quantidade))
    return relatorio

# Simulação no terminal
if __name__ == "__main__":
    # Cadastro de produtos
    print("Cadastrando produtos...")
    cadastrar_produto("001", "Caneta", "Papelaria", 100)
    cadastrar_produto("002", "Caderno", "Papelaria", 50)
    cadastrar_produto("003", "lapis", "Papelaria", 68 )

    # Movimentações
    print("Registrando movimentações...")
    movimentar_produto("Entrada", "001", 20)  # Entrada de 20 unidades de Caneta
    movimentar_produto("Saída", "002", 10)    # Saída de 10 unidades de Caderno

    # Relatório
    print("Gerando relatório...")
    relatorio = gerar_relatorio()
    for id, nome, categoria, quantidade in relatorio:
        print(f"ID: {id}, Nome: {nome}, Categoria: {categoria}, Quantidade: {quantidade}")
