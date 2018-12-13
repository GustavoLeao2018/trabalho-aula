#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def media(n1, n2):
    """ Função para calcular a média entre dois números. """
    return (n1 + n2) / 2


def maior(n1, n2, n3):
    """ Função para calcular o maior entre três números """
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3
