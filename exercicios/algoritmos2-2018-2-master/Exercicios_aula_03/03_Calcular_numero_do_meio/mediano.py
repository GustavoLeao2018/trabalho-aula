#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3

def menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3

def mediano(n1, n2, n3):
    n_maior = maior(n1, n2, n3)
    n_menor = menor(n1, n2, n3)

    if n1 > n_menor and n1 < n_maior:
        return n1
    elif n2 > n_menor and n2 < n_maior:
        return n2
    else:
        return n3
