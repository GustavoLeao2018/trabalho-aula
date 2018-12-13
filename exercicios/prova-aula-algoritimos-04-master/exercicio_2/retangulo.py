#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exercicio 2."""

from pygame import *


class Retangulo:
    """Cria a classe ratangulo"""
    def cria_retangulo(self):
        return draw.rect(self.janela, self.cor, [self.x, self.y, self.largura, self.altura])

    def colidiu(self, ret, retangulo_teste):
        x = retangulo_teste.x
        y = retangulo_teste.y
        largura = retangulo_teste.largura
        altura = retangulo_teste.altura

        if x < self.x or (x + largura) > (self.x + self.largura):
            return False
        elif  y < self.y or (self.y + self.largura) > (self.y + self.altura):
            return False
        else:
            return True

    def __init__(self, x, y, largura, altura, cor, janela):
        """Cria o método construtor."""
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.janela = janela

        self.cria_retangulo()




