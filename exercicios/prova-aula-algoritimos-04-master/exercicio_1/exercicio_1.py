#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercicio 2."""

from pygame import *
from sys import exit
import bola
from random import choice, randint

CORES_LISTA = [
    (255, 0, 0),
    (0, 0, 255),
    (255, 0, 0),
    (255,165,0),
(47,79,79),
(0,250,154),
(0,255,127),
(152,251,152),
(144,238,144),
(143,188,143),
(60,179,113),
(46,139,87),
(0,100,0),
(0,128,0),
(34,139,34),
(50,205,50),
(0,255,0),
(124,252,0),
(127,255,0),
(173,255,47),
(154,205,50),
(107,142,35),
(85,107,47),
(128,128,0),
(189,83,107),
(218,165,32),
(184,134,11),
(139,69,19),
(160,82,45),
(188,143,143),
(205,133,63),
(210,105,30),
(244,164,96),
(255,222,173),
(245,222,179),
(222,184,135),
(210,180,140),
(255,215,0),
(240,230,140),
(255,69,0),
(255,140,0),
(255,165,0)
]

def tela():
    tamanho = largura_tela, altura_tela = (400, 400)

    janela = display.set_mode(tamanho)

    init()

    x = randint(0, largura_tela)
    y = randint(0, altura_tela)
    raio = 5
    largura = 5
    cor = choice(CORES_LISTA)


    clock = time.Clock()

    bol = bola.Bola(janela, x, y, cor, raio, largura)

    while True:
        for evento  in event.get():
            if evento.type == QUIT:
                exit()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    exit()

        x = randint(0, largura_tela)
        y = randint(0, altura_tela)

        bol.reescreve(x, y, bol)

        display.flip()
        clock.tick(10)


if  __name__ == '__main__':
    tela()