import pygame
import sys
import random


pygame.init()


largura, altura = 600, 400
tamanho_celula = 20
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)


cima = (0, -1)
baixo = (0, 1)
esquerda = (-1, 0)
direita = (1, 0)


def jogo_snake():

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Snake Game')


    cobra = [(largura // 2, altura // 2)]
    direcao = direita


    comida = nova_comida()


    velocidade = 10


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direcao != baixo:
                    direcao = cima
                elif evento.key == pygame.K_DOWN and direcao != cima:
                    direcao = baixo
                elif evento.key == pygame.K_LEFT and direcao != direita:
                    direcao = esquerda
                elif evento.key == pygame.K_RIGHT and direcao != esquerda:
                    direcao = direita


        nova_cabeca = (cobra[0][0] + direcao[0] * tamanho_celula, cobra[0][1] + direcao[1] * tamanho_celula)
        cobra.insert(0, nova_cabeca)


        if nova_cabeca == comida:
            comida = nova_comida()
            velocidade += 1
        else:
            cobra.pop()

        if (
            nova_cabeca[0] < 0 or nova_cabeca[0] >= largura or
            nova_cabeca[1] < 0 or nova_cabeca[1] >= altura or
            any(segmento == nova_cabeca for segmento in cobra[1:])
        ):
            pygame.quit()
            sys.exit()


        tela.fill((0, 0, 0))

        for segmento in cobra:
            pygame.draw.rect(tela, cor_cobra, (segmento[0], segmento[1], tamanho_celula, tamanho_celula))

        pygame.draw.rect(tela, cor_comida, (comida[0], comida[1], tamanho_celula, tamanho_celula))

        pygame.display.flip()


        pygame.time.Clock().tick(velocidade)

def nova_comida():
    x = random.randint(0, largura // tamanho_celula - 1) * tamanho_celula
    y = random.randint(0, altura // tamanho_celula - 1) * tamanho_celula
    return x, y

jogo_snake()
