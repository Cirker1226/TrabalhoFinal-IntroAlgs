import pygame
from src.config import *

fonte_titulo = pygame.font.Font("assets/fontes/Eight-Bit Madness.ttf", FONTE_TAMANHO + 20)
fonte_normal = pygame.font.Font("assets/fontes/Eight-Bit Madness.ttf", FONTE_TAMANHO)
fonte_pequena = pygame.font.Font("assets/fontes/Eight-Bit Madness.ttf", FONTE_TAMANHO - 10)

overlay = pygame.Surface((LARGURA, ALTURA))
overlay.set_alpha(120)
overlay.fill((0, 0, 0))

logo = pygame.image.load("assets/imagens/logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (400, 200))

'''
O render — cria uma superfície (imagem) com o texto. Ele não desenha nada na tela ainda, 
só gera o objeto visual, já o blit — cola uma superfície na tela em uma posição específica. 
É o que de fato aparece na tela.
'''

def tela_inicio(tela, fundo_surf):
    tela.blit(fundo_surf, (0, 0))
    tela.blit(overlay, (0, 0))

    tela.blit(logo, (LARGURA // 2 - logo.get_width() // 2, 100))

    instrucao = fonte_normal.render("ENTER para comecar", True, COR_PONTUACAO)
    tela.blit(instrucao, (LARGURA // 2 - instrucao.get_width() // 2, 320))

def tela_gameover(tela, fundo_surf, pontos, recorde):
    tela.blit(fundo_surf, (0, 0))
    tela.blit(overlay, (0, 0))

    game_over = fonte_titulo.render("GAME OVER", True, COR_PONTUACAO)
    tela.blit(game_over, (LARGURA // 2 - game_over.get_width() // 2, 100))

    txt_pontos = fonte_normal.render("PONTOS: " + str(pontos), True, COR_PONTUACAO)
    tela.blit(txt_pontos, (LARGURA // 2 - txt_pontos.get_width() // 2, 200))

    txt_recorde = fonte_pequena.render("REC: " + str(recorde), True, COR_PONTUACAO)
    tela.blit(txt_recorde, (LARGURA // 2 - txt_recorde.get_width() // 2, 260))

    txt_reiniciar = fonte_normal.render("ENTER para reiniciar", True, COR_PONTUACAO)
    tela.blit(txt_reiniciar, (LARGURA // 2 - txt_reiniciar.get_width() // 2, 340))

nave_img = pygame.image.load("assets/imagens/nave.png").convert_alpha()
nave_img = pygame.transform.scale(nave_img, (NAVE_LARGURA, NAVE_ALTURA))

nave_x = LARGURA

vitoria = pygame.image.load("assets/imagens/vitoria.png").convert_alpha()
vitoria = pygame.transform.scale(vitoria, (400, 200))

def resetar_nave():
    global nave_x
    nave_x = LARGURA

def desenhar_nave(tela):
    global nave_x

    destino = LARGURA - nave_img.get_width() // 2
    if nave_x > destino:
        nave_x -= 5
    tela.blit(nave_img, (nave_x, ALTURA // 2 - nave_img.get_height() // 2))

def tela_vitoria(tela, fundo_surf, pontos, recorde):
    tela.blit(fundo_surf, (0, 0))
    tela.blit(overlay, (0, 0))

    tela.blit(vitoria, (LARGURA // 2 - vitoria.get_width() // 2, 60))

    txt_pontos = fonte_normal.render("PONTOS: " + str(pontos), True, COR_PONTUACAO)
    tela.blit(txt_pontos, (LARGURA // 2 - txt_pontos.get_width() // 2, 310))

    txt_recorde = fonte_pequena.render("REC: " + str(recorde), True, COR_PONTUACAO)
    tela.blit(txt_recorde, (LARGURA // 2 - txt_recorde.get_width() // 2, 370))

    txt_sair = fonte_normal.render("ENTER para sair", True, COR_PONTUACAO)
    tela.blit(txt_sair, (LARGURA // 2 - txt_sair.get_width() // 2, 460))