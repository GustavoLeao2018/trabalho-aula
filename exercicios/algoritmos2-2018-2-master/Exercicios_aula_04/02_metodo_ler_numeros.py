#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# EXTRA: Leia um número arbitrário de números digitados pelo usuário,
# pare a entrada de dados quando o usuário entrar com o número zero (0).
"""


def ler_numeros():
    """ Criando a função para popular a lista. """
    lista_numeros = []
    numero = 1
    while numero != 0:
        numero = int(input("Digite um número: "))
        if numero != 0:
            lista_numeros.append(numero)
        else:
            numero = 0
    return lista_numeros


def mostra_lista(x):
    """ Criando metodo para mostrar a lista. """
    for item in x:
        print(item)


# Chamando a função ler_numeros()
lista_impressa = ler_numeros()
mostra_lista(lista_impressa)
