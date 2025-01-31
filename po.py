biblioteca = []
class Livro:
    def __init__(self, autor,titulo,genero):
        self.autor=autor
        self.titulo=titulo
        self.emprestimo=False
        self.genero=genero
        self.data_deemprestimo=None

def add_livro(biblioteca):
    autor=input("Digite o autor")
    livro=input("Digite o nome do Livro")
    genero=input("Digite o Genero")
    biblioteca.append(Livro(autor,livro,genero))
    print("Livro adicionado com sucesso!")

def remover_livro(biblioteca):
    titulo=input("Digite o Título do Livro que deseja remover")
    for livro in biblioteca:
        if livro.titulo == titulo:
            biblioteca.remove(livro)
            print("LIVRO removido!!")
            return
    print("Não encontrei o Livro")

def buscar_Livro(biblioteca):
    titulo=input("Digite o titulo do  livro que você deseja encontrar")
    for  livro in biblioteca:
        if livro.titulo == titulo:
            print(f"O Livro {livro.titulo} foi encontrado!")
            return
    print("Não encontrei")

def Todos_livors(biblioteca):
 if not biblioteca:
     print("Não ha livros")
 else:
     for livro in biblioteca:
         print(f"Autor: {livro.autor} Titulo: {livro.titulo} Genero:  {livro.genero}")

def emprestar_livro(biblioteca):
    titulo=input("Digite o titulo do livro que deseja emprestar")
    for livro in biblioteca:
        if livro.titulo == titulo:
            if not livro.emprestimo:
                livro.emprestimo= True
                livro.data_deemprestimo=input("Digite a data de devolução (DD/MM/AAAA): ")
                print("Livro emprestado com sucesso!")
            else:
                print("O livro já está emprestado.")
            return
    print("Livro não encontrado.")

def Menu():
    while True:
        
        print("1 para add livro")
        print("2 para remover livro")
        print("3 para buscar livro")
        print("4 para exibir todos os livros")
        print("5 para emprestar livro")
        print("6 para sair do sistema ")
        opção= input("Excolha uma opção meu nobre")
        if opção == "1":
            add_livro(biblioteca)
        elif opção=="2":
            remover_livro(biblioteca)
        elif opção=="3":
            buscar_Livro(biblioteca)
        elif opção=="4":
            Todos_livors(biblioteca)
        elif opção=="5":
            emprestar_livro(biblioteca)
        elif opção=="6":
            print("Saindo do sitema....")
            break
        else:
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    Menu()
            



