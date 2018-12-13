#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Escreva um método que receba uma lista
e retorne outra lista que diz se cada número
da lista original é par (True) ou ímpar (False). """

# Aqui eu importo apenas a funcao (randint) do modulo random
from random import randint

# Aqui a lista esta esta sendo populada
lista_original = [randint(0, 100) for item in range(randint(10, 100))]


def lista_par_ou_impar(lista_original):
    """
    Criando o metodo recebendo os dados da lista_original
    Comparando cada item para saber se é True ou False
    """
    true_ou_false = []
    for item in lista_original:
        if (item % 2) == 0:
            true_ou_false.append(True)
        else:
            true_ou_false.append(False)
    # A lista_final contem os valores True ou False
    return true_ou_false


# Chamando o metodo (lista_par_ou_impar) que recebe a lista_original
# como parametro
lista_true_ou_false = lista_par_ou_impar(lista_original)
conta_item = 0
for item in lista_true_ou_false:
    # Imprime na tela cada item da lista_true_ou_false
    print(item)
    conta_item += 1
