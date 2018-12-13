#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercicio 2."""

from pygame import *
from sys import exit
import retangulo
from random import randint, choice

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
    tamanho = largura, altura = (400, 400)

    janela = display.set_mode(tamanho)

    init()

    quantidade = 10
    x = [randint(0, largura) for x in range(quantidade)]
    y = [randint(0, altura) for x in range(quantidade)]

    largura = [randint(10, 50) for x in range(quantidade)]
    altura = [randint(10, 50) for x in range(quantidade)]

    cores = [choice(CORES_LISTA) for x in range(quantidade)]


    while  True:
        for evento  in event.get():
            if evento.type == QUIT:
                exit()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    exit()

        retangulos = []
        for cont in range(quantidade):
            ret = retangulo.Retangulo(x[cont], y[cont], altura[cont], largura[cont], cores[cont], janela)
            if cont != 0:
                contador = cont - 1
                if ret.colidiu(ret, retangulos[contador]) == True:
                    while ret.colidiu(ret, retangulos[contador]) == True:
                        ret = retangulo.Retangulo(x[cont], y[cont], altura[cont], largura[cont], cores[cont], janela)

            retangulos.append(ret)

        display.flip()


if  __name__ == '__main__':
    tela()