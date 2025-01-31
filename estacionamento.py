concesionaria=[]
def add_carro(nome,placa,ano):
    carro={
        "nome":nome,
        "placa":placa,
        "ano":ano
    }
    concesionaria.append(carro)
    print(f"O carro {carro['nome']}: foi adicionado")
def exibir_carro():
    for carro in concesionaria:
            print(f"LISTA DE CARROS: {carro['nome']}, Placa {carro['placa']},  Ano {carro['ano']}")
    else:
            if carro not in concesionaria:
                 print("sem carros")

exibir_carro()
