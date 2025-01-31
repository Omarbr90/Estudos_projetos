import sqlite3

# Conectar ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect("estoque.db")
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL,
        validade TEXT NOT NULL
    )
''')
conn.commit()


def adicionar():
    nome = input("Qual o nome do produto? ")
    preco = input("Qual o preço do produto? ")
    quantidade = int(input("Qual a quantidade do produto? "))
    validade = input("Qual a data de validade do produto? ")

    cursor.execute("INSERT INTO produtos (nome, preco, quantidade, validade) VALUES (?, ?, ?, ?)",
                   (nome, preco, quantidade, validade))
    conn.commit()
    print("O produto foi adicionado com sucesso!")


def exibir_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        print("Não há produtos cadastrados.")
    else:
        print("\nLISTA DE PRODUTOS:")
        for p in produtos:
            print(f"ID: {p[0]}, Nome: {p[1]}, Preço: R${p[2]:.2f}, Quantidade: {p[3]}, Validade: {p[4]}")
        print("")


def buscar_produto():
    nome = input("Insira o nome do produto que deseja buscar: ")
    cursor.execute("SELECT * FROM produtos WHERE nome = ?", (nome,))
    produto = cursor.fetchone()

    if produto:
        print(f"Produto encontrado! ID: {produto[0]}, Nome: {produto[1]}, Preço: R${produto[2]:.2f}, "
              f"Quantidade: {produto[3]}, Validade: {produto[4]}")
    else:
        print("Produto não encontrado.")


def remover():
    nome = input("Insira o nome do produto que deseja remover: ")
    cursor.execute("DELETE FROM produtos WHERE nome = ?", (nome,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")


def atualizar_estoque():
    nome = input("Insira o nome do produto que deseja atualizar: ")
    nova_qtd = int(input("Insira a nova quantidade do produto: "))

    cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (nova_qtd, nome))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Estoque do produto '{nome}' atualizado para {nova_qtd}.")
    else:
        print("Produto não encontrado.")


def menu():
    while True:
        print("\n1 - Adicionar Produto")
        print("2 - Exibir Produtos")
        print("3 - Buscar Produto")
        print("4 - Remover Produto")
        print("5 - Atualizar Estoque")
        print("6 - Sair")
        print("---------------------")
        op = input("Escolha uma opção: ")

        if op == "1":
            adicionar()
        elif op == "2":
            exibir_produtos()
        elif op == "3":
            buscar_produto()
        elif op == "4":
            remover()
        elif op == "5":
            atualizar_estoque()
        elif op == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

# Fechar a conexão quando o programa terminar
conn.close()
