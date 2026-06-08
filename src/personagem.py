import pygame
from src.config import *

sprites = [
    pygame.image.load("assets/imagens/personagem/tile000.png"),
    pygame.image.load("assets/imagens/personagem/tile001.png"),
    pygame.image.load("assets/imagens/personagem/tile002.png"),
    pygame.image.load("assets/imagens/personagem/tile003.png"),
    pygame.image.load("assets/imagens/personagem/tile004.png"),
    pygame.image.load("assets/imagens/personagem/tile005.png"),
    pygame.image.load("assets/imagens/personagem/tile006.png"),
    pygame.image.load("assets/imagens/personagem/tile007.png"),
    pygame.image.load("assets/imagens/personagem/tile008.png"),
    pygame.image.load("assets/imagens/personagem/tile009.png"),
    pygame.image.load("assets/imagens/personagem/tile010.png")
]

sprites = [
    pygame.transform.scale(
        sprite,
        (PERSONAGEM_LARGURA, PERSONAGEM_ALTURA)
    )
    for sprite in sprites
]

frame = 0
contador_animacao = 0

x = PERSONAGEM_X
y = PERSONAGEM_Y

velocidade_y = 0
pulando = False

def atualizar():
    global y, velocidade_y, pulando
    global frame, contador_animacao

    contador_animacao += 1

    if contador_animacao >= VELOCIDADE_ANIMACAO:
        contador_animacao = 0
        frame += 1

        if frame >= len(sprites):
            frame = 0

    velocidade_y += GRAVIDADE
    y += velocidade_y

    if y >= CHAO:
        y = CHAO
        velocidade_y = 0
        pulando = False

def pular():
    global velocidade_y, pulando

    if not pulando:
        velocidade_y = FORCA_PULO
        pulando = True

def desenhar(tela):
    tela.blit(sprites[frame], (x, y))