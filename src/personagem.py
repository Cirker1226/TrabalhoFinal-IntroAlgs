import pygame
from src.config import *

'''
Pense como plano cartesiano, o Y representa a forma vertical
do jogo enquanto o X representa a forma horizontal do jogo.
'''

sprites = [
    pygame.image.load("assets/imagens/personagem/tile000.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile001.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile002.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile003.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile004.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile005.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile006.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile007.png").convert_alpha()
]

sprites = [
    pygame.transform.scale(
        sprite,
        (PERSONAGEM_LARGURA, PERSONAGEM_ALTURA)
    )
    for sprite in sprites
]

sprites_agachado = [
    pygame.image.load("assets/imagens/personagem/tile008.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile009.png").convert_alpha(),
    pygame.image.load("assets/imagens/personagem/tile010.png").convert_alpha()
]

sprites_agachado = [
    pygame.transform.scale(
        sprite,
        (PERSONAGEM_LARGURA_AGACHADO, PERSONAGEM_ALTURA_AGACHADO)
    )
    for sprite in sprites_agachado
]

frame = 0
contador_animacao = 0

x = PERSONAGEM_X
y = PERSONAGEM_Y

velocidade_y = 0
pulando = False
agachado = False

def atualizar():
    global y, velocidade_y, pulando
    global frame, contador_animacao

    if not pulando:
        contador_animacao += 1

        if contador_animacao >= VELOCIDADE_ANIMACAO:
            contador_animacao = 0
            frame += 1

            limite = len(sprites_agachado) if agachado else len(sprites)
            if frame >= limite:
                frame = 0

    velocidade_y += GRAVIDADE
    y += velocidade_y

    if y >= CHAO:
        y = CHAO
        velocidade_y = 0
        pulando = False

def pular():
    global velocidade_y, pulando

    if not pulando and not agachado:
        velocidade_y = FORCA_PULO
        pulando = True

def agachar():
    global agachado, frame

    if not pulando:
        if not agachado:
            frame = 0
        agachado = True

def levantar():
    global agachado, frame

    agachado = False
    frame = 0

def sprite_atual():
    if agachado:
        return sprites_agachado[frame % len(sprites_agachado)]
    return sprites[frame]

def desenhar(tela):
    sprite = sprite_atual()

    if agachado:
        y_desenho = y + (PERSONAGEM_ALTURA - sprite.get_height())
        tela.blit(sprite, (x, y_desenho))
    else:
        tela.blit(sprite, (x, y))

def get_rect():
    sprite = sprite_atual()
    largura = sprite.get_width()
    altura = sprite.get_height()

    if agachado:
        y_rect = y + (PERSONAGEM_ALTURA - altura)
    else:
        y_rect = y

    return pygame.Rect(
        x + PERSONAGEM_HITBOX_MARGEM_X,
        y_rect + PERSONAGEM_HITBOX_MARGEM_Y,
        largura - 2 * PERSONAGEM_HITBOX_MARGEM_X,
        altura - 2 * PERSONAGEM_HITBOX_MARGEM_Y
    )

def desenhar_hitbox(tela):
    pygame.draw.rect(tela, (0, 255, 0), get_rect(), 2, border_radius=10)

def caminhar_direita():
    global x
    x += 3

def get_x():
    return x