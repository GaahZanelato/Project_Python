import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações do jogo
largura, altura = 800, 600
cor_fundo = (135, 206, 250)  # Azul-claro para o céu
cor_mario = (255, 0, 0)  # Vermelho para o Mario

# Inicializar a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Mario em Python')

# Carregar a imagem do Mario
mario_img = pygame.image.load('flappy_bird.png.jpg')  # Substitua 'mario.png' pelo caminho correto da imagem
mario_img = pygame.transform.scale(mario_img, (50, 50))

# Inicializar a posição do Mario
posicao_mario = [100, altura - 100]

# Velocidade e gravidade do Mario
velocidade_mario = 5
gravidade = 1
pulo = -15
pulando = False

# Relógio para controle de frames
relogio = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not pulando:
                velocidade_mario = pulo
                pulando = True

    # Atualizar posição do Mario
    posicao_mario[1] += velocidade_mario
    velocidade_mario += gravidade

    # Verificar se o Mario atingiu o chão
    if posicao_mario[1] > altura - 100:
        posicao_mario[1] = altura - 100
        pulando = False

    # Desenhar na tela
    tela.fill(cor_fundo)
    tela.blit(mario_img, posicao_mario)

    # Atualizar a tela
    pygame.display.flip()

    # Controlar os frames por segundo
    relogio.tick(30)
