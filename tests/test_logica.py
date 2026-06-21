import os

# Precisa rodar antes de importar os modulos do jogo, que carregam imagem/fonte
# assim que sao importados.

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame
pygame.init()
pygame.display.set_mode((1, 1))

import src.alien as alien
import src.cenario as cenario
import src.personagem as personagem
import src.pontos as pontos_modulo
import src.telas as telas
from src.config import LARGURA, VELOCIDADE_FUNDO, FORCA_PULO


def test_get_dificuldade_comeca_no_nivel_1():
    """Deve retornar dificuldade 1 quando a pontuacao ainda e baixa."""
    pontos_modulo.pontos = 0
    assert pontos_modulo.get_dificuldade() == 1


def test_pular_ativa_o_estado_de_pulando():
    """Deve marcar o personagem como pulando e aplicar a forca de pulo."""
    personagem.pulando = False
    personagem.agachado = False
    personagem.pular()
    assert personagem.pulando is True
    assert personagem.velocidade_y == FORCA_PULO


def test_atualizar_move_o_fundo_para_esquerda():
    """Deve mover o fundo para a esquerda de acordo com a velocidade configurada."""
    cenario.x_fundo = 100
    cenario.atualizar()
    assert cenario.x_fundo == 100 - VELOCIDADE_FUNDO


def test_resetar_limpa_a_lista_de_obstaculos():
    """Deve esvaziar a lista de obstaculos do alien apos o reset."""
    alien.obstaculos.append({"tipo": 1, "x": 0, "y": 0, "largura": 1, "altura": 1, "frame": 0, "contador_animacao": 0})
    alien.resetar()
    assert alien.obstaculos == []


def test_resetar_nave_volta_para_fora_da_tela():
    """Deve reposicionar a nave para fora da tela, pronta para reentrar."""
    telas.nave_x = 200
    telas.resetar_nave()
    assert telas.nave_x == LARGURA