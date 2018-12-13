from No import No

class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None

    def pop(self):
        if self.final is not None:
            iterador = self.inicial
            while iterador is not None:
                if iterador.proximo is None:
                    break
                iterador = iterador.proximo
            iterador.anterior.proximo = None
            return iterador

    def remove_first(self):
        if self.final is not None:
            self.inicial = self.inicial.proximo
            self.inicial.anterior = None

    def append(self, valor):
        if self.inicial is None and self.final is None:
            self.inicial = self.final = No(valor)
        else:
            self.final.proximo = no = No(valor)
            no.anterior = self.final
            self.final = self.final.proximo

    def add_first(self, valor):
        no = No(valor)
        no.proximo = self.inicial
        self.inicial = no

        proximo = self.inicial.proximo
        proximo.anterior = no

    def __str__(self):
        texto = "#" * 70 + "\n"
        iterador = self.inicial
        while iterador is not None:
            texto += str(iterador) + "\n"
            iterador = iterador.proximo
        texto += "#" *70
        return texto





