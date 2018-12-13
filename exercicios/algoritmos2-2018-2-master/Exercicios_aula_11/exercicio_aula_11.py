#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exercício aula 11 - Lista Encadeada. """

"""
Implementação de lista encadeada:
- addFirst(valor) : Insere um valor no início da lista. ok
- removeFirst(): Remove um malor do início da lista. ok
- removeLast(): Remove um valor do final da lista.
"""


class No:
    """Define um no da lista encadeada."""
    def __init__(self, valor):
        """Inicializa no."""
        self.valor = valor
        self.proximo_no = None

    def __str__(self):
        return "{} -> {}".format(self.valor, self.proximo_no)


class Lista:
    """ Define lista encadeada."""
    def __init__(self):
        """
        - Inicializa uma nova lista. Esta classe tem dois ponteiros.
        - self.head: aponta para o primeiro no
        - self.tail: aponta para o último no
        - se lista vazia: ambos apontam para "None"
        """
        # Ponteiro do início da lista
        self.head = None
        # ponteiro do fim da lista
        self.tail = None
        self.size = 0

    def __repr__(self):
        return "A lista é: [ {} ] -> Tamanho: {} Nós".format(
            self.head, self.size)

    def size(self):
        return self.size

    def append(self, valor):
        """Adiciona um valor ao final da lista."""
        # Cria um novo objeto do tipo "no" recebendo valor
        novo_no = No(valor)
        if self.head is None:  # se verdade - lista está vazia
            self.head = self.tail = novo_no
        else:
            # executa se já houver algum item na lista
            self.tail.proximo_no = novo_no
            self.tail = novo_no
        self.size += 1

    def addFirst(self, valor):
        """Insere um valor no início da lista."""
        # Cria um novo objeto do tipo "no" recebendo valor
        novo_no = No(valor)
        if self.head is None:  # se verdade - lista está vazia
            self.head = self.tail = novo_no
        else:
            novo_no.proximo_no = self.head
            self.head = novo_no
        self.size += 1

    def removeFirst(self):
        """Remove um valor do início da lista."""
        # primeiro verifico se a lista está vazia
        if self.head is None:
            print("Erro: a lista está vazia.")
        # se a lista não estiver vazia
        # armazenamos o valor do primeiro "nó"
        else:
            valor_primeiro_no = self.head.valor
            if self.head is self.tail:  # se True: a lista tem apenas "1 item"
                self.head = self.tail = None
            else:  # se a lista tiver mais de "1 item"
                self.head = self.head.proximo_no
            print("Removendo primeiro item: [ {} ]".format(valor_primeiro_no))
            self.size -= 1
            return valor_primeiro_no

    def removeLast(self):
        """Remove um valor do final da lista."""
        # primeiro verifico se a lista está vazia
        if self.head is None:
            print("Erro: a lista está vazia.")
        # se a lista não estiver vazia
        # armazenamos o valor do primeiro "nó"
        else:
            valor_ultimo_no = self.tail.valor
            if self.head is self.tail:  # se True: a lista tem apenas "1 item"
                self.head = self.tail = None
            else:  # se a lista tiver mais de "1 item"
                no_atual = self.head
                while no_atual.proximo_no is not self.tail:
                    no_atual = no_atual.proximo_no
                no_atual.proximo_no = None
                self.tail = no_atual
            print("Removendo último item: [ {} ]".format(valor_ultimo_no))
            self.size -= 1
            return valor_ultimo_no


print("\nTESTANDO A LISTA")
print("="*40)
lista = Lista()
# lista.append(10)
# lista.append(27)
# lista.append(1000)
# lista.addFirst(2121)
# lista.append(311)
# lista.append(2755)
print(lista)
"""Removendo valores"""
lista.removeFirst()
lista.removeLast()
print(lista)
