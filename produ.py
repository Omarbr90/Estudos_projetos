produtos=[]
class Produto:
    def __init__(self,nome,preço,quantidade):
        self.nome=nome
        self.quantidade=quantidade
        self.preço=preço

def add_pordu(produtos):
    nome= input("Qual o nome de seu produto")
    preço= input("Qual o preço de seu produto")
    quantidade= input("Qual a quantiade do  seu produto")
    produtos.append(Produto(nome,preço,quantidade))
    print("O produto foi salvo na lista")

def remover(produtos):
    nome=input("Digite o nome do produto que deseja remover")
    for produto in produtos:
        if produto.nome==nome:
            produtos.remove(produto)
            print("Produto removido!!")
            return
    print("Não encontrei o produto")   

def exibir(produtos):
    if not produtos:
            print("Não temos produtos")
    else:
        for produto in produtos:
            print(f"Nome: {produto.nome} Preço: {produto.preço} Quantidae: {produto.quantidade}")



# def
add_pordu(produtos)
exibir(produtos)