import itertools
from collections import Counter

def solicitar_jogos():
    jogos = []
    for i in range(1, 3):
        while True:
            try:
                entrada = input(f"Digite os 15 números do jogo {i} (sem espaços, ex: 010203...): ").strip()
                if len(entrada) != 30 or not entrada.isdigit():
                    print("Você deve digitar exatamente 15 números, cada um com dois dígitos (ex: 010203...).")
                    continue
                jogo = [int(entrada[j:j + 2]) for j in range(0, len(entrada), 2)]
                if any(n < 1 or n > 25 for n in jogo):
                    print("Todos os números devem estar entre 01 e 25.")
                    continue
                jogos.append(jogo)
                break
            except ValueError:
                print("Erro na entrada. Certifique-se de digitar 15 números corretamente.")
    return jogos

def calcular_frequencia(jogos):
    frequencia = Counter(num for jogo in jogos for num in jogo)
    total = sum(frequencia.values())
    frequencia_normalizada = {num: freq / total for num, freq in frequencia.items()}
    return frequencia, frequencia_normalizada

def gerar_combinacoes_possiveis():
    numeros = list(range(1, 26))
    return itertools.combinations(numeros, 15)

def filtrar_combinacoes(combinacoes, frequencia, frequencia_normalizada):
    combinacoes_filtradas = []
    media_frequencia = sum(frequencia.values()) / len(frequencia)

    for combinacao in combinacoes:
        score_frequencia = sum(
            frequencia_normalizada.get(num, 0) * 3 if frequencia.get(num, 0) > media_frequencia else frequencia_normalizada.get(num, 0)
            for num in combinacao
        )
        
        # Penalizar consecutivos, múltiplos e simétricos
        penalizacao_consecutivos = sum(1 for i in range(len(combinacao) - 1) if combinacao[i] + 1 == combinacao[i + 1])
        penalizacao_multiplos = sum(1 for i in range(len(combinacao) - 1) if combinacao[i] % 2 == combinacao[i + 1] % 2)
        ajuste_extremos = abs(sum(1 for n in combinacao if n <= 8) - sum(1 for n in combinacao if n >= 18))
        
        # Score final
        score_total = score_frequencia - (penalizacao_consecutivos + penalizacao_multiplos + ajuste_extremos * 0.5)
        combinacoes_filtradas.append((combinacao, score_total))
    
    combinacoes_filtradas.sort(key=lambda x: x[1], reverse=True)
    return combinacoes_filtradas[:10]

def main():
    print("Bem-vindo ao gerador de possíveis jogos!")
    
    jogos = solicitar_jogos()
    frequencia, frequencia_normalizada = calcular_frequencia(jogos)
    combinacoes = gerar_combinacoes_possiveis()
    melhores_jogos = filtrar_combinacoes(combinacoes, frequencia, frequencia_normalizada)
    
    print("\nPossíveis jogos baseados na análise dos últimos sorteios:")
    for i, (jogo, score) in enumerate(melhores_jogos, 1):
        print(f"Jogo {i}: {jogo} (Score: {score:.2f})")

if __name__ == "__main__":
    main()
