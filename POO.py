armazem=[]
class Produto:
    def __init__(self,nome,preço,quantidade,validade):
        self.nome=nome
        self.preço=preço
        self.quantidade=quantidade
        self.validade=validade


def adicionar(armazem):
        nome=input("qual o nome de seu produto")
        preço=input("qual o preço de seu produto")
        quantidade=input("qual a quantidade  de seu produto")
        validade=input("qual a data de validade produto")
        armazem.append(Produto(nome,preço,quantidade,validade))
        print("O produto foi adicionado")

   
def exibir_produto(armazem):
        if not armazem:
            print("Não ha produtos")
        else:
            for i in armazem:
                print(f"LISTA DE PRODUTOS: Nome: {i.nome} Preço: {i.preço} Quantidade: {i.quantidade} Validade: {i.validade}")
    
    
def buscar_produto(armazem):
        nome=input("Insira o nome do produto que deseja buscar")
        for j in armazem:
            if j.nome==nome:
                print(f"O produto {j.nome} foi encontrado")
                return 
        print("Não encontrei")
    
    
def remover(armazem):
        re=input("Insira o nome do produto que deseja REMOVER")
        for produto in armazem:
            if produto.nome==re:
                armazem.remove(produto)
                print("Produto removido")
                return
        print("Não encontrei")


def atualizr_estoque(armazem):
    nome=input("Insira o nome do produto que deseja buscar")
    for j in armazem:
            if j.nome==nome:
                novaqtn= int (input("Insira a nova quantidade do produto"))
                j.quantidade=novaqtn
                print(f"O estoque do produto {j.nome} foi atualizado para {novaqtn}")
                return
    print("Não foi encontrado")
                 
     
     
def menu():
        while True:
            print("1 para add Produto:")
            print("___________________")
            print("2 para Exibir produto:")
            print("___________________")
            print("3 para buscar Produto:")
            print("___________________")
            print("4 para REmover produto:")
            print("___________________")
            print("5 Atualizar o estoque : ")
            print("___________________")
            print("6 Para sair ...... : ")
            print("___________________")
            op =input("Escolha uma opção:")
            print("___________________")
            if op=="1":
                adicionar(armazem)
            elif op=="2":
                exibir_produto(armazem)
            elif op =="3":
                buscar_produto(armazem)
            elif op=="4":
                remover(armazem)
            elif op=="5":
                atualizr_estoque(armazem)
            elif op=="6":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")            
if __name__=="__main__":
    menu()