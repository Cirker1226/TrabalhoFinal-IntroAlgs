import pygame

from src.config import *
import src.personagem as personagem
import src.cenario as fundo

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Alien Escape")

clock = pygame.time.Clock()

rodando = True

while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                personagem.pular()

    fundo.atualizar()
    personagem.atualizar()

    fundo.desenhar(tela)
    personagem.desenhar(tela)

    pygame.display.flip()

pygame.quit()