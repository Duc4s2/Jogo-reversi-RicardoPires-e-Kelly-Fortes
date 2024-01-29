import pygame
import sys


# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
Vermelho =(255,0,0)
Azul =(0,0,255)
# Tamanho do tabuleiro
TAMANHO_TABULEIRO = 8

# Tamanho de cada célula do tabuleiro
TAMANHO_CELULA = 50

# Inicializa o Pygame
pygame.init()

# Configura o tamanho da janela
tamanho_janela = (TAMANHO_TABULEIRO * TAMANHO_CELULA, TAMANHO_TABULEIRO * TAMANHO_CELULA)
janela = pygame.display.set_mode(tamanho_janela)

# Cria o tabuleiro
tabuleiro = [[None for _ in range(TAMANHO_TABULEIRO)] for _ in range(TAMANHO_TABULEIRO)]
tabuleiro[3][3] = tabuleiro[4][4] = PRETO
tabuleiro[3][4] = tabuleiro[4][3] = BRANCO

# Define o jogador atual
jogador_atual = BRANCO

# Função para verificar se um movimento é válido
def movimento_valido(i, j, jogador):
    # Verifica se a posição está dentro do tabuleiro e está vazia
    if i < 0 or i >= TAMANHO_TABULEIRO or j < 0 or j >= TAMANHO_TABULEIRO or tabuleiro[i][j] is not None:
        return False

    # Verifica todas as direções a partir da posição
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue

            # Começa a partir da posição atual
            x, y = i + di, j + dj

            # Verifica se a próxima posição está dentro do tabuleiro e contém uma peça do oponente
            if x >= 0 and x < TAMANHO_TABULEIRO and y >= 0 and y < TAMANHO_TABULEIRO and tabuleiro[x][y] == (BRANCO if jogador == PRETO else PRETO):
                # Continua movendo na mesma direção
                while True:
                    x += di
                    y += dj

                    # Se saiu do tabuleiro, então não é um movimento válido
                    if x < 0 or x >= TAMANHO_TABULEIRO or y < 0 or y >= TAMANHO_TABULEIRO:
                        break

                    # Se encontrou uma peça do jogador atual, então é um movimento válido
                    if tabuleiro[x][y] == jogador:
                        return True

    # Se nenhuma direção é válida, então não é um movimento válido
    return False

# Função para atualizar o tabuleiro após um movimento
def atualizar_tabuleiro(i, j, jogador):
    # Coloca a peça do jogador na posição
    tabuleiro[i][j] = jogador

    # Verifica todas as direções a partir da posição
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue

            # Começa a partir da posição atual
            x, y = i + di, j + dj

            # Verifica se a próxima posição está dentro do tabuleiro e contém uma peça do oponente
            if x >= 0 and x < TAMANHO_TABULEIRO and y >= 0 and y < TAMANHO_TABULEIRO and tabuleiro[x][y] == (BRANCO if jogador == PRETO else PRETO):
                # Continua movendo na mesma direção
                while True:
                    x += di
                    y += dj

                    # Se saiu do tabuleiro, então não é um movimento válido
                    if x < 0 or x >= TAMANHO_TABULEIRO or y < 0 or y >= TAMANHO_TABULEIRO:
                        break

                    # Se encontrou uma peça do jogador atual, então é um movimento válido
                    if tabuleiro[x][y] == jogador:
                        # Captura as peças do oponente
                        x -= di
                        y -= dj
                        while tabuleiro[x][y] == (BRANCO if jogador == PRETO else PRETO):
                            tabuleiro[x][y] = jogador
                            x -= di
                            y -= dj
                        break

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            i, j = x // TAMANHO_CELULA, y // TAMANHO_CELULA
            if movimento_valido(i, j, jogador_atual):
                atualizar_tabuleiro(i, j, jogador_atual)
                jogador_atual = BRANCO if jogador_atual == PRETO else PRETO

    # Desenha o tabuleiro
    for i in range(TAMANHO_TABULEIRO):
        for j in range(TAMANHO_TABULEIRO):
            pygame.draw.rect(janela, Vermelho if (i + j) % 2 == 0 else Azul, pygame.Rect(i*TAMANHO_CELULA, j*TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
            if tabuleiro[i][j] is not None:
                pygame.draw.circle(janela, tabuleiro[i][j], (i*TAMANHO_CELULA + TAMANHO_CELULA//2, j*TAMANHO_CELULA + TAMANHO_CELULA//2), TAMANHO_CELULA//2 - 5)

    # Atualiza a janela
    pygame.display.flip()