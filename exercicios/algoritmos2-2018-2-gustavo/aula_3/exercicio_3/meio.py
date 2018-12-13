#!/usr/bin/env python3
#-*- coding: utf-8 -*-


def maior_de_tres(a, b, c):
    """Verifica qual o maior entre três números."""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c