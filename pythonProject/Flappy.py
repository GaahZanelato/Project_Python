import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Configurações do jogo
largura, altura = 800, 600
gravidade = 1
velocidade_inicial = -15
largura_cano = 80
espaco_canos = 200
fases = [(200, 5), (150, 4), (100, 3)]  # Lista de fases com altura do cano e número de canos

# Cores
cor_fundo = (135, 206, 250)
cor_passaro = (255, 255, 0)
cor_cano = (34, 139, 34)

# Inicializar a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Flappy Bird')

# Carregar a imagem do Flappy Bird
flappy_bird_img = pygame.image.load('flappy_bird.png.jpg')
flappy_bird_img = pygame.transform.scale(flappy_bird_img, (50, 50))

# Função para reiniciar o jogo
def reiniciar_jogo():
    global passaro, velocidade_passaro, canos, fase_atual, pontuacao
    passaro = pygame.Rect(50, altura // 2 - 25, 50, 50)
    velocidade_passaro = velocidade_inicial
    fase_atual = 0
    pontuacao = 0
    gerar_fase()

# Função para gerar uma nova fase
def gerar_fase():
    global canos
    canos = []
    altura_fase, num_canos = fases[fase_atual]
    for i in range(num_canos):
        altura_cano = random.randint(50, altura_fase - 50)
        novo_cano = pygame.Rect(largura + i * largura_cano * 2, 0, largura_cano, altura_cano)
        cano_inferior = pygame.Rect(largura + i * largura_cano * 2, altura_cano + espaco_canos, largura_cano, altura - (altura_cano + espaco_canos))
        canos.extend([novo_cano, cano_inferior])

# Inicializar o passaro e os canos
reiniciar_jogo()

# Fonte para a pontuação
fonte = pygame.font.Font(None, 36)

# Relógio para controle de frames
relogio = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                velocidade_passaro = velocidade_inicial

    # Atualizar posição do passaro
    passaro.y += velocidade_passaro
    velocidade_passaro += gravidade

    # Atualizar posição dos canos
    for cano in canos:
        cano.x -= 5  # Velocidade dos canos

        # Se um cano sair da tela, reposicioná-lo
        if cano.right < 0:
            altura_fase, num_canos = fases[fase_atual]
            altura_cano = random.randint(50, altura_fase - 50)
            cano.x += num_canos * largura_cano * 2
            cano.height = altura_cano if cano.height == 0 else altura - (altura_cano + espaco_canos)

    # Verificar colisões com os canos
    for cano in canos:
        if passaro.colliderect(cano):
            reiniciar_jogo()

    # Verificar se o passaro saiu da tela
    if passaro.top <= 0 or passaro.bottom >= altura:
        reiniciar_jogo()

    # Verificar pontuação
    if canos and canos[0].right == passaro.left:
        pontuacao += 1

    # Avançar para a próxima fase
    if pontuacao > 0 and pontuacao % 5 == 0:
        fase_atual = min(fase_atual + 1, len(fases) - 1)
        gerar_fase()

    # Desenhar na tela
    tela.fill(cor_fundo)
    for cano in canos:
        pygame.draw.rect(tela, cor_cano, cano)

    # Desenhar o passaro
    tela.blit(flappy_bird_img, (passaro.x, passaro.y))

    # Desenhar a pontuação
    mensagem_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
    tela.blit(mensagem_pontuacao, (10, 10))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar os frames por segundo
    relogio.tick(30)
