import os
alunos=[]
notas=[]
def adicionar_aluno(nome, notas):
    media=sum(notas) /len(notas)
    aluno={
        "nome":nome,
        "notas":notas,
        "media": media
    }
    alunos.append(aluno)
    print(f"O aluno {aluno['nome']}: notas {aluno['notas']}: media: {aluno['media']} foi adicionado")
n= float(input("Digite sua nota"))
for n  in notas:
    float(input("Digite sua nota"))
    i=input("vc tem mais notas ")
    if i == "sim":
        n
    else:
        break
adicionar_aluno("omar",[10,9])
adicionar_aluno("oma",[10,5])
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
try:
    def salvar_em_arquivo():
        inf = "alunosss.txt"
        with open(inf,"w") as arquivo:
            for aluno in alunos:
                linha= f"{aluno['nome']} {aluno['media']:.2f}\n"
            arquivo.write(linha)
            print(f"as infomaçoes do {inf} foram salvas")
        salvar_em_arquivo()  
except ValueError:
    print("valor erdado")
finally:
    print("sitema encerrado")    















# def salvar_em_arquivo():
#     arquivo_nome = "alunosss.txt"
#     with open(arquivo_nome, "w") as arquivo:
#         for aluno in alunos:
#             linha = f"{aluno['nome']},{aluno['media']:.2f}\n"
#             arquivo.write(linha)
#     print(f"Informações salvas no arquivo '{arquivo_nome}'.")
# salvar_em_arquivo()

       
    

    
