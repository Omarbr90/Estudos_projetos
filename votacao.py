def sistema_de_votacao():
    opcoes = ["Opção 1", "Opção 2", "Opção 3"]
    votos = [0] * len(opcoes)
    votacao_ativa = True

    print("Sistema de Votação")
    print("As opções são:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")

    while votacao_ativa:
        try:
            escolha = int(input(f"Escolha uma opção (1-{len(opcoes)}) ou 0 para finalizar a votação: "))
            
            if escolha == 0:
                votacao_ativa = False
            elif 1 <= escolha <= len(opcoes):
                votos[escolha - 1] += 1
                print(f"Você votou na {opcoes[escolha - 1]}")
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

    print("\nResultados da Votação:")
    for i, opcao in enumerate(opcoes):
        print(f"{opcao}: {votos[i]} voto(s)")

if __name__ == "__main__":
    sistema_de_votacao()
