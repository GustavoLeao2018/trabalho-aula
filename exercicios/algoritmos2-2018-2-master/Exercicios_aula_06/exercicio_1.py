#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exercicio aula 06. """

"""
Criando um jogo com o PyGame
Instale, se você ainda não instalou a biblioteca PyGame,
com o comando (use "python" ou "python3"):

python3 -m pip install -U pygame --user
Crie um programa que inicie uma janela no tamanho 800 x 600,
com o título "PyGame Tutorial",
e encerre o programa ao teclar "ESC".
"""

#  sintaxe da TUPLA
#  tupla = (valor1, valorn)  ou tupla = (valor1,)
from pygame import *
from sys import exit

tamanho = largura, altura = (800, 600)
janela = display.set_mode(tamanho)

# nomear janela
display.set_caption("Exercício 06")
init()

while True:
    for evento in event.get():
        # QUIT é um evento (constante)  do PyGame
        if evento.type == QUIT:
            exit()
        if evento.type == KEYDOWN:
            if evento.key == K_ESCAPE:
                exit()
            # if evento.key == K_t:
            #     print("Digitou T")
drawn.cicle(janela, (255,0,0), [10, 10], 5, 5)
display.flip()
