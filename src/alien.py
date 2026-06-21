import pygame
import random
import src.pontos as pontuacao
from src.config import *

'''
Pense como plano cartesiano, o Y representa a forma vertical
do jogo enquanto o X representa a forma horizontal do jogo.
'''

sprites_alien1 = [
    pygame.image.load("assets/imagens/aliens/1-1.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/1-2.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/1-3.png").convert_alpha()
]

sprites_alien2 = [
    pygame.image.load("assets/imagens/aliens/2-1.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/2-2.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/2-3.png").convert_alpha()
]

sprites_alien3 = [
    pygame.image.load("assets/imagens/aliens/4-1.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/4-2.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/4-3.png").convert_alpha()
]

sprites_ovni = [
    pygame.image.load("assets/imagens/aliens/3-1.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/3-2.png").convert_alpha(),
    pygame.image.load("assets/imagens/aliens/3-3.png").convert_alpha()
]

sprites_alien1[0] = pygame.transform.scale(sprites_alien1[0], (ALIEN1_LARGURA, ALIEN1_ALTURA))
sprites_alien1[1] = pygame.transform.scale(sprites_alien1[1], (ALIEN1_LARGURA, ALIEN1_ALTURA))
sprites_alien1[2] = pygame.transform.scale(sprites_alien1[2], (ALIEN1_LARGURA, ALIEN1_ALTURA))

sprites_alien2[0] = pygame.transform.scale(sprites_alien2[0], (ALIEN2_LARGURA, ALIEN2_ALTURA))
sprites_alien2[1] = pygame.transform.scale(sprites_alien2[1], (ALIEN2_LARGURA, ALIEN2_ALTURA))
sprites_alien2[2] = pygame.transform.scale(sprites_alien2[2], (ALIEN2_LARGURA, ALIEN2_ALTURA))

sprites_alien3[0] = pygame.transform.scale(sprites_alien3[0], (ALIEN2_LARGURA, ALIEN2_ALTURA))
sprites_alien3[1] = pygame.transform.scale(sprites_alien3[1], (ALIEN2_LARGURA, ALIEN2_ALTURA))
sprites_alien3[2] = pygame.transform.scale(sprites_alien3[2], (ALIEN2_LARGURA, ALIEN2_ALTURA))

sprites_ovni[0] = pygame.transform.scale(sprites_ovni[0], (OVNI_LARGURA, OVNI_ALTURA))
sprites_ovni[1] = pygame.transform.scale(sprites_ovni[1], (OVNI_LARGURA, OVNI_ALTURA))
sprites_ovni[2] = pygame.transform.scale(sprites_ovni[2], (OVNI_LARGURA, OVNI_ALTURA))

sprites = {
    1: sprites_alien1,
    2: sprites_alien2,
    3: sprites_alien3,
    4: sprites_ovni,
}

DIMENSOES = {
    1: (ALIEN1_LARGURA, ALIEN1_ALTURA),
    2: (ALIEN2_LARGURA, ALIEN2_ALTURA),
    3: (ALIEN2_LARGURA, ALIEN2_ALTURA),
    4: (OVNI_LARGURA, OVNI_ALTURA),
}

obstaculos = []

contador_spawn = 0
proximo_spawn = random.randint(INTERVALO_MIN_OBSTACULO, INTERVALO_MAX_OBSTACULO)

def criar_obstaculo():
    tipo = random.choice(list(sprites.keys()))
    largura, altura = DIMENSOES[tipo]

    if tipo == 4:
        y = OVNI_Y
    else:
        y = (CHAO + PERSONAGEM_ALTURA) - altura

    obstaculos.append({
        "tipo": tipo,
        "x": LARGURA,
        "y": y,
        "largura": largura,
        "altura": altura,
        "frame": 0,
        "contador_animacao": 0
    })

def atualizar():
    global contador_spawn, proximo_spawn

    dificuldade = pontuacao.get_dificuldade()
    velocidade = ALIEN_VELOCIDADE + dificuldade
    intervalo_min = max(30, INTERVALO_MIN_OBSTACULO - dificuldade * 10)
    intervalo_max = max(60, INTERVALO_MAX_OBSTACULO - dificuldade * 20)

    contador_spawn += 1
    if contador_spawn >= proximo_spawn:
        contador_spawn = 0
        proximo_spawn = random.randint(intervalo_min, intervalo_max)
        criar_obstaculo()

    for obstaculo in obstaculos:
        obstaculo["x"] -= velocidade

        obstaculo["contador_animacao"] += 1
        if obstaculo["contador_animacao"] >= VELOCIDADE_ANIMACAO_ALIEN:
            obstaculo["contador_animacao"] = 0
            obstaculo["frame"] += 1

            total_frames = len(sprites[obstaculo["tipo"]])
            if obstaculo["frame"] >= total_frames:
                obstaculo["frame"] = 0

    vivos = []
    for o in obstaculos:
        if o["x"] + o["largura"] > 0:
            vivos.append(o)
    obstaculos[:] = vivos

def desenhar(tela):
    for obstaculo in obstaculos:
        sprite = sprites[obstaculo["tipo"]][obstaculo["frame"]]
        tela.blit(sprite, (obstaculo["x"], obstaculo["y"]))

def desenhar_hitbox(tela):
    for obstaculo in obstaculos:
        rect = get_rect(obstaculo)
        pygame.draw.rect(tela, (255, 0, 0), rect, 2, border_radius=10)

def verificar_colisao(rect_personagem):
    for obstaculo in obstaculos:
        rect_obstaculo = get_rect(obstaculo)

        if rect_personagem.colliderect(rect_obstaculo):
            return True

    return False

MARGENS = {
    1: ALIEN1_HITBOX_MARGEM,
    2: ALIEN2_HITBOX_MARGEM,
    3: ALIEN3_HITBOX_MARGEM,
    4: OVNI_HITBOX_MARGEM,
}

def get_rect(obstaculo):
    margem = MARGENS.get(obstaculo["tipo"], 0)

    return pygame.Rect(
        obstaculo["x"] + margem,
        obstaculo["y"] + margem,
        obstaculo["largura"] - 2 * margem,
        obstaculo["altura"] - 2 * margem
    )

def resetar():
    global obstaculos, contador_spawn, proximo_spawn
    obstaculos = []
    contador_spawn = 0
    proximo_spawn = random.randint(INTERVALO_MIN_OBSTACULO, INTERVALO_MAX_OBSTACULO)