import pygame
from src.config import *

fundo = pygame.image.load("assets/imagens/fundo.png")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

x_fundo = 0

def atualizar():
    global x_fundo

    x_fundo -= VELOCIDADE_FUNDO

    if x_fundo <= -LARGURA:
        x_fundo = 0

def desenhar(tela):
    tela.blit(fundo, (x_fundo, 0))
    tela.blit(fundo, (x_fundo + LARGURA, 0))