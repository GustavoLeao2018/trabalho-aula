#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Crie uma classe Bola com os campos: centro, raio e cor.

Crie um programa que mostre uma janela com 400 x 400 pixels,
onde a bola fica batendo nos limites da janela,
trocando de cor e invertendo a direção
cada vez que bater nos limintes. Por exemplo,
ao bater no limite esquerdo da janela,
a bola passará a mover-se para a direita, ao bater no limite superior,
passará a mover-se para baixo.
"""

from sys import exit
import pygame
pygame.init()


# Criando janela
tamanho_janela = largura, altura = (900, 800)
janela = pygame.display.set_mode(tamanho_janela)

# Criando o circulo
vermelho = (255, 0, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)
raio_circulo = 10
posicao_x = 10
posicao_x_final = 200
posicao_y = 190
movimento_em_x = 20
movimento_em_y = 5
clock = pygame.time.Clock()

# Enquanto usuario nao clicar (fechar janeta)
# ou nao digitar ESC, a janela fica aberta
pygame.display.set_caption("Algorítmos 2 - Pergunta 01")
while True:
    clock.tick(10)
    for evento in pygame.event.get():
        # QUIT é um evento (constante)  do PyGame
        if evento.type == pygame.QUIT:
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                exit()

    posicao_x += movimento_em_x
    posicao_y += movimento_em_y

    pygame.draw.circle(janela, vermelho, (posicao_x, posicao_y), raio_circulo)
    pygame.display.flip()
