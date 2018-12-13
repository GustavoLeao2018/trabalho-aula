#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class No:
    def __init__(self, valor):
        self._dado = valor
        self.proximo = None
        self.anterior = None
        self.salto_1 = None
        self.salto_2 = None
        self.salto_3 = None

    @property
    def dado(self):
        return self._dado

    def __str__(self):
        if self.proximo is None and self.anterior is None:
            return f"Anterior: {self.anterior} | Nó: {self.dado} | Próximo: {self.proximo} "
        if self.proximo is not None and self.anterior is None:
            return f"Anterior: {self.anterior} | Nó: {self.dado} | Próximo: {self.proximo.dado} "
        if self.proximo is None and self.anterior is not None:
            return f"Anterior: {self.anterior.dado} | Nó: {self.dado} | Próximo: {self.proximo} "
        if self.proximo is not None and self.anterior is not None:
            return f"Anterior: {self.anterior.dado} | Nó: {self.dado} | Próximo: {self.proximo.dado} "