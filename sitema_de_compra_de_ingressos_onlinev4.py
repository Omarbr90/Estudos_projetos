eventos = []
proximoid = 1

def geraid():
    global proximoid
    return f"PY{proximoid}"

def adicionar_evento(nome, data, local, ingressos):
    global proximoid
    evento = {
        "Nome": nome,
        "Data": data,
        "ID": geraid(),
        "Local": local,
        "Ingressos": ingressos
    }
    eventos.append(evento)
    proximoid += 1
    print("Evento adicionado com sucesso!")

def comprar_ingresso(id, quantidade):
    if not eventos:
        print("Nenhum evento cadastrado")
        return
    
    for evento in eventos:
        if evento["ID"] == id:
            if evento["Ingressos"] > 0:
                if evento["Ingressos"] >= quantidade:
                    confirmacao = input(f"Confirmar compra para o evento {evento['Nome']}? (s/n): ")
                    if confirmacao.lower() == "s":
                        evento["Ingressos"] -= quantidade
                        print("Compra confirmada!")
                    else:
                        print("Compra recusada.")
                else:
                    print("Quantidade de ingressos indisponível.")
            else:
                print("Ingressos esgotados.")
            break
    else:
        print("Evento não encontrado.")

def editar_evento():
    if not eventos:
        print("Nenhum evento cadastrado")
        return
    
    id = input("Digite o ID do evento que deseja editar: ")
    for evento in eventos:
        if evento["ID"] == id:
            evento["Nome"] = input("Digite o novo nome do evento: ")
            evento["Data"] = input("Digite a nova data do evento: ")
            evento["Local"] = input("Digite o novo local do evento: ")
            evento["Ingressos"] = int(input("Digite a nova quantidade de ingressos: "))
            print(f"Evento {id} alterado com sucesso!")
            break
    else:
        print(f"Evento de ID {id} não encontrado.")

def exibir_eventos():
    if not eventos:
        print("Não há eventos cadastrados.")
    else:
        for evento in eventos:
            print(f"Nome: {evento['Nome']}, Data: {evento['Data']}, ID: {evento['ID']}, Local: {evento['Local']}, Ingressos: {evento['Ingressos']}")

def buscar_evento(id):
    if not eventos:
        print("Nenhum evento cadastrado")
        return
    
    for evento in eventos:
        if evento["ID"] == id:
            print(evento)
            break
    else:
        print("Evento não encontrado.")

def remover_evento(id):
    if not eventos:
        print("Nenhum evento cadastrado")
        return
    
    for evento in eventos:
        if evento["ID"] == id:
            eventos.remove(evento)
            print("Evento removido com sucesso!")
            break
    else:
        print("Evento não encontrado.")

def menu():
    while True:
        try:
            print("\nSistema de Compra de Ingressos Online")
            escolha = int(input(
                "1. Adicionar Evento\n"
                "2. Comprar Ingresso\n"
                "3. Editar Evento\n"
                "4. Exibir Eventos\n"
                "5. Buscar Evento\n"
                "6. Remover Evento\n"
                "7. Sair\n"
                "Escolha: "
            ))
            if escolha == 1:
                nome = input("Nome do evento: ")
                data = input("Data do evento: ")
                local = input("Local do evento: ")
                ingressos = int(input("Quantidade de ingressos: "))
                adicionar_evento(nome, data, local, ingressos)
            elif escolha == 2:
                id = input("ID do evento: ")
                quantidade = int(input("Quantidade de ingressos: "))
                comprar_ingresso(id, quantidade)
            elif escolha == 3:
                editar_evento()
            elif escolha == 4:
                exibir_eventos()
            elif escolha == 5:
                id = input("ID do evento: ")
                buscar_evento(id)
            elif escolha == 6:
                id = input("ID do evento: ")
                remover_evento(id)
            elif escolha == 7:
                print("Encerrando o sistema...")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

menu()
