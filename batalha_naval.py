# Batalha Naval - Nível Básico

# 1. Representa o Tabuleiro (10x10) preenchido com água (0)
def criar_tabuleiro(tamanho=10):
    return [[0] * tamanho for _ in range(tamanho)]


# 2. Função para posicionar navio no tabuleiro
def posicionar_navio(tabuleiro, linha, coluna, orientacao, tamanho=3):
    if orientacao == "H":  # Horizontal
        for c in range(coluna, coluna + tamanho):
            tabuleiro[linha][c] = 3
    elif orientacao == "V":  # Vertical
        for l in range(linha, linha + tamanho):
            tabuleiro[l][coluna] = 3


# 3. Exibir tabuleiro no console com cabeçalho de coordenadas
def exibir_tabuleiro(tabuleiro):
    tamanho = len(tabuleiro)

    # Cabeçalho das colunas
    print("   ", end="")
    for c in range(tamanho):
        print(c, end=" ")
    print()

    # Linha separadora
    print("   " + "--" * tamanho)

    # Linhas do tabuleiro
    for i, linha in enumerate(tabuleiro):
        print(f"{i:2}|", end=" ")
        for valor in linha:
            print(valor, end=" ")
        print()
    print()


# Função principal
def main():
    # Criar tabuleiro
    tabuleiro = criar_tabuleiro()

    # Coordenadas fixas dos navios
    # Navio 1: horizontal (linha 2, coluna 4)
    posicionar_navio(tabuleiro, linha=2, coluna=4, orientacao="H")

    # Navio 2: vertical (linha 5, coluna 6)
    posicionar_navio(tabuleiro, linha=5, coluna=6, orientacao="V")

    # Exibir o tabuleiro final
    print("Tabuleiro Final:")
    exibir_tabuleiro(tabuleiro)


# Executar
if __name__ == "__main__":
    main()
