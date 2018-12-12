#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from No import No


class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None
        self.quantidade_de_itens = 0
        self.saltar = False

    def append(self, valor):
        if self.inicial is None and self.final is None:
            self.inicial = self.final = No(valor)
        else:
            self.final.proximo = no = No(valor)
            no.anterior = self.final
            self.final = self.final.proximo
        self.quantidade_de_itens += 1
        self._organize()

    def pop(self):
        if self.final is not None:
            iterador = self.inicial
            while iterador is not None:
                if iterador.proximo is None:
                    break
                iterador = iterador.proximo
            iterador.anterior.proximo = None
        self.quantidade_de_itens -= 1
        self.saltar = False
        self._organize()
        return iterador

    def remove_first(self):
        if self.final is not None:
            self.inicial = self.inicial.proximo
            self.inicial.anterior = None
        self.quantidade_de_itens -= 1
        self.saltar = False
        self._organize()

    def add_first(self, valor):
        no = No(valor)
        no.proximo = self.inicial
        self.inicial = no

        proximo = self.inicial.proximo
        proximo.anterior = no
        self.quantidade_de_itens -= 1
        self.saltar = False
        self._organize()

    def _organize(self):
        iterador = self.inicial
        anterior = None
        while iterador is not None:
            if iterador is not None:
                if anterior is not None:
                    print()
                    print("Iterador: "+str(iterador.dado))
                    print("Anterior: "+str(anterior.dado))
                    print()    
                    if iterador.dado < anterior.dado:
                        print()
                        print("Iterador: "+str(iterador.dado))
                        print("Anterior: "+str(anterior.dado))
                        print()    
            anterior = iterador            
            iterador = iterador.proximo

    def search(self, valor):
        print("#" * 100)
        if self.saltar is False:
            salto_1 = self.quantidade_de_itens // 2
            salto_2 = salto_1 // 2
            salto_3 = salto_2 // 2
            print(f"Quantidade de itens: {self.quantidade_de_itens}")
            print(f"Salto 1: {salto_1}")
            print(f"Salto 2: {salto_2}")
            print(f"Salto 3: {salto_3}")

            iterador = self.inicial
            cont = 0
            lista_salto_1 = []
            lista_salto_2 = []
            lista_salto_3 = []

            while iterador is not None:
                if (cont % salto_1) == 0:
                    lista_salto_1.append(iterador)
                if (cont % salto_3) == 0:
                    lista_salto_3.append(iterador)
                cont += 1
                iterador = iterador.proximo

            iterador = self.final
            cont = 0
            while iterador is not None:
                if (iterador.dado % salto_2) == 0:
                    lista_salto_2.append(iterador)

                cont += 1
                iterador = iterador.anterior

            for i, item in enumerate(lista_salto_1):
                if i == 0:
                    self.inicial.salto_1 = item
                else:
                    anterior.salto_1 = item
                anterior = item
            for i, item in enumerate(lista_salto_3):
                if i == 0:
                    self.inicial.salto_3 = item
                else:
                    anterior.salto_3 = item
                anterior = item
            for i, item in enumerate(reversed(lista_salto_2)):
                if i == 0:
                    self.final.salto_2 = item
                else:
                    anterior.salto_2 = item


                anterior = item
            self.saltar = True

        iterador = self.inicial.salto_1
        while iterador is not None:
            if iterador.proximo is not None:
                if valor == iterador.proximo.dado:
                    print(f"{valor} <  {str(iterador.proximo.dado)} = {valor == iterador.proximo.dado}")
            if iterador.anterior is not None:
                if valor == iterador.anterior.dado:
                    print(f"{valor} <  {str(iterador.anterior.dado)} = {valor == iterador.anterior.dado}")
            if valor == iterador.dado:
                print(f"{str(iterador.dado)} ==  {valor} = {valor == iterador.dado}")
                break
            if valor < iterador.dado:
                print(f"{valor} <  {str(iterador.dado)} = {valor < iterador.dado}")
                if valor == iterador.anterior.dado:
                    print(f"{str(iterador.anterior.dado)} ==  {valor} = {valor == iterador.anterior.dado}")
                    break
                if valor is not iterador.anterior.dado:

                    iterador_volta = iterador.anterior
                    while iterador_volta.anterior:
                        if valor == iterador_volta.dado:
                            print(f"{str(iterador_volta.dado)} ==  {valor} = {valor == iterador_volta.dado}")
                            break

                        iterador_volta = iterador_volta.anterior
                    break

            iterador = iterador.salto_1
        print("#" * 100)

    def __str__(self):
        # iterador = self.inicial
        # texto = "#" * 20 + "[Lista:]" + "#" * 20 + "\n"
        # while iterador is not None:
        #     texto += f"{str(iterador)}\n"
        #     if iterador.salto_1 is not None:
        #         texto += f"\u001b[32m-> Salto 1: {iterador.salto_1} \u001b[0m\n"
        #     if iterador.salto_2 is not None:
        #         texto += f"\u001b[33m--> Salto 2: {iterador.salto_2} \u001b[0m\n"
        #     if iterador.salto_3 is not None:
        #         texto += f"\u001b[34m---> Salto 3: {iterador.salto_3} \u001b[0m\n"
        #     iterador = iterador.proximo
        # texto += f"Tamanho: {self.quantidade_de_itens} \n"
        # texto += "#" * 20 + "#" * 5 + "#" * 20
        # return texto

        iterador = self.inicial
        texto = "#" * 20 + "[Lista:]" + "#" * 20 + "\n"
        while iterador is not None:
            texto += f"{str(iterador)}\n"
            if iterador.salto_1 is not None:
                texto += f"\u001b[33m {iterador.dado} \u001b[0m\n"
                texto += f"\u001b[34m--> Salto 2: {iterador.salto_1} \u001b[0m\n"
            if iterador.salto_2 is not None:
                texto += f"\u001b[31m {iterador.dado} \u001b[0m\n"
                texto += f"\u001b[33m--> Salto 2: {iterador.salto_2} \u001b[0m\n"
            if iterador.salto_3 is not None:
                texto += f"\u001b[31m {iterador.dado} \u001b[0m\n"
                texto += f"\u001b[32m--> Salto 2: {iterador.salto_3} \u001b[0m\n"
            iterador = iterador.proximo
        texto += f"Tamanho: {self.quantidade_de_itens} \n"
        texto += "#" * 20 + "#" * 5 + "#" * 20
        return texto
