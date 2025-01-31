#---QUESTÃO 1 - Sistema de Gestão de Notas de Alunos--
import os
alunos=[]
def adicionar_aluno(nome,notas):
    media= sum(notas) / len(notas)
    aluno={
        "nome":nome,
        "notas":notas,
        "media":media,
    }
    alunos.append(aluno)
    print(f"O aluno: {aluno['nome']} foi adicionado. Suas notas foram {aluno['notas']}. A média foi: {aluno['media']}.")
nome = input("Digite o nome do aluno: ")
notas=[]
for i in range(2,6):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)
    continuar = input("Deseja adicionar outra nota? (s/n): ")
    if continuar.lower() != 's':
        break
adicionar_aluno("Omar",[8.5,9.5])
adicionar_aluno("João",[10,9.9])
def ordenar_alunos(alunos):
    n = len (alunos)
    for i in range(n - 1):
        for j in range(n - i - 1):
             if alunos[j]["media"] < alunos[j + 1]["media"]:
                  alunos[j], alunos[j + 1] = alunos[j + 1], alunos[j]
    print("Alunos ordenados por média:")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Média: {aluno['media']}")
ordenar_alunos(alunos)
def salvar_arquivo():
    file_path = "resultado_alunos.txt"
    if os.path.exists(file_path):
        escolha = input("O arquivo já existe. Deseja sobrescrever? (s/n): ")
        if escolha.lower() != 's':
            print("Operação cancelada.")
            return
    try:
        with open(file_path, "w") as file:
            file.write("Alunos ordenados por média:\n")
            for aluno in alunos:
                file.write(f"Nome: {aluno['nome']}, Média: {aluno['media']}\n")
        print("Dados salvos com sucesso no arquivo.")
    except IOError:
        print("Erro ao salvar o arquivo. Verifique as permissões ou o espaço disponível em disco.")
salvar_arquivo()
#--QUESTÃO 2 - Biblioteca de Livros Digitais --
livros = []
def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")

    while True:
        try:
            ano = int(input("Digite o ano de publicação do livro: "))
            if ano > 0:
                break
            else:
                print("Erro: o ano deve ser um número positivo.")
        except ValueError:
            print("Erro: por favor, insira um número inteiro válido.")

    while True:
        try:
            paginas = int(input("Digite o número de páginas do livro: "))
            if paginas > 0:
                break
            else:
                print("Erro: o número de páginas deve ser um número positivo.")
        except ValueError:
            print("Erro: por favor, insira um número inteiro válido.")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "paginas": paginas
    }
    livros.append(livro)
    print(f"O livro '{titulo}' foi adicionado com sucesso.")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\nLista de Livros:")
    for livro in livros:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Páginas: {livro['paginas']}")

def ordenar_livros():
    if not livros:
        print("Nenhum livro cadastrado para ordenar.")
        return

    criterio = input("Deseja ordenar por ano de publicação ou número de páginas? (ano/paginas): ").lower()
    if criterio not in ["ano", "paginas"]:
        print("Opção inválida. Tente novamente.")
        return

    ordem = input("Deseja ordenar em ordem crescente ou decrescente? (crescente/decrescente): ").lower()
    reverso = ordem == "decrescente"

    livros.sort(key=lambda x: x[criterio], reverse=reverso)
    print("Livros ordenados com sucesso.")
    listar_livros()
def salvar_livros():
    try:
        with open("biblioteca.txt", "w") as file:
            for livro in livros:
                linha = f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['paginas']}\n"
                file.write(linha)
        print("Dados salvos com sucesso no arquivo 'biblioteca.txt'.")
    except IOError:
        print("Erro ao salvar o arquivo. Verifique as permissões ou o espaço disponível em disco.")
def carregar_livros():
    if not os.path.exists("biblioteca.txt"):
        print("Nenhum arquivo de biblioteca encontrado para carregar.")
        return

    try:
        with open("biblioteca.txt", "r") as file:
            for linha in file:
                titulo, autor, ano, paginas = linha.strip().split(",")
                livro = {
                    "titulo": titulo,
                    "autor": autor,
                    "ano": int(ano),
                    "paginas": int(paginas)
                }
                livros.append(livro)
        print("Dados carregados com sucesso do arquivo 'biblioteca.txt'.")
    except IOError:
        print("Erro ao ler o arquivo. Verifique as permissões ou o espaço disponível em disco.")
    except ValueError:
        print("Erro ao processar os dados do arquivo. Verifique o formato do arquivo.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Ordenar livros")
        print("4. Salvar dados")
        print("5. Carregar dados")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            ordenar_livros()
        elif opcao == "4":
            salvar_livros()
        elif opcao == "5":
            carregar_livros()
        elif opcao == "6":
            if input("Deseja salvar os dados antes de sair? (s/n): ").lower() == "s":
                salvar_livros()
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()
#--QUESTÃO 3: Sistema de Gestão de Estoque de Loja--
produtos = []
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")

    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco > 0:
                break
            else:
                print("Erro: o preço deve ser um número positivo.")
        except ValueError:
            print("Erro: por favor, insira um valor numérico válido para o preço.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade >= 0:
                break
            else:
                print("Erro: a quantidade deve ser um número inteiro não negativo.")
        except ValueError:
            print("Erro: por favor, insira um valor inteiro válido para a quantidade.")

    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print(f"O produto '{nome}' foi adicionado com sucesso.")
def atualizar_quantidade():
    listar_produtos()
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    
    for produto in produtos:
        if produto["nome"].lower() == nome_produto.lower():
            while True:
                try:
                    ajuste = int(input("Digite a quantidade para adicionar (positivo) ou remover (negativo): "))
                    nova_quantidade = produto["quantidade"] + ajuste
                    if nova_quantidade >= 0:
                        produto["quantidade"] = nova_quantidade
                        print(f"A nova quantidade de '{produto['nome']}' é {produto['quantidade']}.")
                        return
                    else:
                        print("Erro: a quantidade não pode ser negativa.")
                except ValueError:
                    print("Erro: por favor, insira um número inteiro válido.")
            break
    else:
        print("Produto não encontrado.")
def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\nLista de Produtos:")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
def ordenar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado para ordenar.")
        return

    criterio = input("Deseja ordenar por preço ou quantidade? (preco/quantidade): ").lower()
    if criterio not in ["preco", "quantidade"]:
        print("Opção inválida. Tente novamente.")
        return

    ordem = input("Deseja ordenar em ordem crescente ou decrescente? (crescente/decrescente): ").lower()
    reverso = ordem == "decrescente"

    produtos.sort(key=lambda x: x[criterio], reverse=reverso)
    print("Produtos ordenados com sucesso.")
    listar_produtos()
def salvar_estoque():
    try:
        with open("estoque.txt", "w") as file:
            for produto in produtos:
                linha = f"{produto['nome']},{produto['categoria']},{produto['preco']},{produto['quantidade']}\n"
                file.write(linha)
        print("Estoque salvo com sucesso no arquivo 'estoque.txt'.")
    except IOError:
        print("Erro ao salvar o arquivo. Verifique as permissões ou o espaço disponível em disco.")
def carregar_estoque():
    if not os.path.exists("estoque.txt"):
        print("Nenhum arquivo de estoque encontrado para carregar.")
        return

    try:
        with open("estoque.txt", "r") as file:
            for linha in file:
                nome, categoria, preco, quantidade = linha.strip().split(",")
                produto = {
                    "nome": nome,
                    "categoria": categoria,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                }
                produtos.append(produto)
        print("Estoque carregado com sucesso do arquivo 'estoque.txt'.")
    except IOError:
        print("Erro ao ler o arquivo. Verifique as permissões ou o espaço disponível em disco.")
    except ValueError:
        print("Erro ao processar os dados do arquivo. Verifique o formato do arquivo.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Atualizar quantidade")
        print("3. Listar produtos")
        print("4. Ordenar produtos")
        print("5. Salvar estoque")
        print("6. Carregar estoque")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_quantidade()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            ordenar_produtos()
        elif opcao == "5":
            salvar_estoque()
        elif opcao == "6":
            carregar_estoque()
        elif opcao == "7":
            if input("Deseja salvar o estoque antes de sair? (s/n): ").lower() == "s":
                salvar_estoque()
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()

