import pygame
from random import randint
from src.config import *

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Alien Escape")

import src.personagem as personagem
import src.cenario as fundo
import src.alien as alien
import src.pontos as pontuacao
import src.telas as telas

clock = pygame.time.Clock()

INICIO = "inicio"
JOGANDO = "jogando"
GAMEOVER = "gameover"
VITORIA = "vitoria"
NAVE = "nave"

PONTUACAO_VITORIA = randint(500, 800)

estado = INICIO

while True:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:

            if estado == INICIO:
                if evento.key == pygame.K_RETURN:
                    estado = JOGANDO

            elif estado == JOGANDO:
                if evento.key == pygame.K_SPACE:
                    personagem.pular()
                if evento.key in (pygame.K_DOWN, pygame.K_LCTRL):
                    personagem.agachar()

            elif estado == GAMEOVER:
                if evento.key == pygame.K_RETURN:
                    alien.resetar()
                    pontuacao.resetar()
                    estado = JOGANDO

            elif estado == VITORIA:
                if evento.key == pygame.K_RETURN:
                    pygame.quit()
                    exit()

        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_DOWN, pygame.K_LCTRL):
                personagem.levantar()

    fundo.atualizar()

    if estado == JOGANDO:
        personagem.atualizar()
        alien.atualizar()
        pontuacao.atualizar()

        if alien.verificar_colisao(personagem.get_rect()):
            pontuacao.salvar_recorde()
            estado = GAMEOVER

        if pontuacao.pontos >= PONTUACAO_VITORIA:
            pontuacao.salvar_recorde()
            telas.resetar_nave()
            estado = NAVE

    elif estado == NAVE:
        personagem.atualizar()
        pontuacao.atualizar()
        personagem.caminhar_direita()

    fundo.desenhar(tela)

    if estado == INICIO:
        telas.tela_inicio(tela, fundo.fundo)

    elif estado == JOGANDO:
        personagem.desenhar(tela)
        alien.desenhar(tela)
        pontuacao.desenhar(tela)
        personagem.desenhar_hitbox(tela)
        alien.desenhar_hitbox(tela)

    elif estado == GAMEOVER:
        personagem.desenhar(tela)
        alien.desenhar(tela)
        telas.tela_gameover(tela, fundo.fundo, pontuacao.pontos, pontuacao.recorde)

    elif estado == NAVE:
        personagem.desenhar(tela)
        pontuacao.desenhar(tela)
        telas.desenhar_nave(tela)
        if personagem.get_x() >= LARGURA // 2:
            estado = VITORIA

    elif estado == VITORIA:
        telas.tela_vitoria(tela, fundo.fundo, pontuacao.pontos, pontuacao.recorde)

    pygame.display.flip()