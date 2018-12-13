#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercicio 1."""

from pygame import *


class Bola:
    """Cria a classe ratangulo"""
    def cria_bola(self):
        return draw.circle(self.janela, self.cor, [self.x, self.y], self.raio, self.largura)


    def reescreve(self, x, y, bol):
        x_bol = bol.x
        y_bol = bol.yr



    def __init__(self, janela, x, y, cor, raio, largura):
        """Cria o método construtor."""
        self.x = x
        self.y = y
        self.largura = largura
        self.raio = raio
        self.cor = cor
        self.janela = janela

        self.cria_bola()
