import pygame
from src.config import *

fonte = pygame.font.Font("assets/fontes/Eight-Bit Madness.ttf", FONTE_TAMANHO)
fonte_recorde = pygame.font.Font("assets/fontes/Eight-Bit Madness.ttf", FONTE_TAMANHO)

pontos = 0
contador = 0
recorde = 0

def carregar_recorde():
    global recorde
    try:
        arquivo = open("data/recorde.txt", "r")
        recorde = int(arquivo.read())
        arquivo.close()
    except:
        recorde = 0

def get_dificuldade():
    if pontos < 300:
        return 1
    elif pontos < 450:
        return 2
    elif pontos < 600:
        return 3
    else:
        return 4

def salvar_recorde():
    global recorde
    if pontos > recorde:
        recorde = pontos
        arquivo = open("data/recorde.txt", "w")
        arquivo.write(str(pontos))
        arquivo.close()

def atualizar():
    global pontos, contador
    contador += 1
    if contador >= VELOCIDADE_PONTUACAO:
        contador = 0
        pontos += 1

def resetar():
    global pontos, contador
    if pontos > 0:
        salvar_recorde()
    pontos = 0
    contador = 0

def desenhar(tela):
    texto = fonte.render(f"{pontos:05d}", True, COR_PONTUACAO)
    rect = texto.get_rect(topright=(LARGURA - MARGEM_PONTUACAO, MARGEM_PONTUACAO))
    tela.blit(texto, rect)

    rec_texto = fonte_recorde.render(f"REC {recorde:05d}", True, COR_PONTUACAO)
    rec_rect = rec_texto.get_rect(topright=(rect.right, rect.bottom + 4))
    tela.blit(rec_texto, rec_rect)

carregar_recorde()