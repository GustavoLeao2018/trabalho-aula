#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exercício aula 12 - Lista Encadeada. """

"""
Implementação de lista encadeada:
- size(): retorna o número de elementos armazenados na lista.
    Ex.: i = lista.size()
- remove(X): remove todos os elementos com o valor X da lista.
    Ex.: lista.remove(5)
- append(X): adiciona o elemento X ao final da lista.
    Ex.: lista.append(5) ok
- addFirst(X): adiciona o elemento X no início da lista.
    Ex.: lista.addFirst(3) ok
- pop(): remove o elemento no final da lista e o retorna ao chamador.
    Ex.: i = lista.pop() ok
- removeFirst(): remove o elemento no início da lista.
    Ex.: lista.removeFirst() ok
- first(): retorna o primeiro elemento da lista.
    Ex.: iterador = lista.first() ok
- last(): retorna o ultimo elemento da lista.
    Ex.: iterador = iterador.last() ok
"""


class No:
    """Define um no da lista encadeada."""
    def __init__(self, valor):
        """Inicializa no."""
        self.valor = valor
        self.proximo_no = None

    def __str__(self):
        return "{} -> {}".format(self.valor, self.proximo_no)


class ListaEncadeada:
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
        """Retorna o tamanho da lista."""  # ainda não funcionou
        return self.size

    def remove(self, valor):
        """Remove todos os elementos com o valor X da lista."""
        # primeiro verifico se a lista está vazia
        if self.head is None:
            print("Erro: a lista está vazia.")
            return self.size
        # Se houver apenas 1 elemento na lista
        if self.head.valor == valor:
            self.head = self.head.proximo_no
        else:
            # Procurando a posição do elemento a ser removido.
            no_anterior = None
            no_atual = self.head
            while no_atual and no_atual.valor != valor:
                no_anterior = no_atual
                no_atual = no_atual.proximo_no
            # O nodo corrente é o nodo a ser removido.
            if no_atual:
                no_anterior.proximo_no = no_atual.proximo_no
            else:
                # O nodo corrente é a cauda da lista.
                no_anterior.proximo_no = None

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

    def pop(self):
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

    def first(self):
        """Retorna o primeiro elemento da lista."""
        return self.head

    def last(self):
        """Retorna o ultimo elemento da lista."""
        return self.tail


print("\nTESTANDO A LISTA")
print("="*40)
lista = ListaEncadeada()
lista.append(10)
lista.append(27)
lista.append(1000)
lista.addFirst(2121)
lista.append(311)
lista.append(10)
# lista.append(2755)
print(lista)
# """Removendo valores"""
# lista.removeFirst()
# lista.pop()
# print(lista)
# print(lista.first().valor)
# print(lista.last().valor)
lista.remove(10)
print(lista)
# print("Iterando a lista")
# iterador = lista.first()
# while iterador is not None:
#     print(iterador.valor)
#     iterador = iterador.proximo_no
