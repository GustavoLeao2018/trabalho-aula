from No import No
class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None

    def add_first(self, valor):
        no = No(valor)
        no.proximo = self.inicial
        self.inicial = no

    def append(self, valor):
        if self.inicial is None and self.final is None:
            self.inicial = self.final = No(valor)
        else:
            self.final.proximo = No(valor)
            self.final = self.final.proximo

    def __str__(self):
        texto = "#"*30+"\n"
        iterador = self.inicial
        while iterador is not None:
            texto += str(iterador)+"\n"
            iterador = iterador.proximo
        texto += "#"*30
        return texto

    def values(self):
        lista = []
        iterador = self.inicial
        while iterador is not None:
            lista.append(iterador.dado)
            iterador = iterador.proximo
        return lista

    def pop(self):
        if self.final is not  None:
            iterador = self.inicial
            anterior = None
            while iterador is not None:
                if iterador.proximo is None:
                    break
                anterior = iterador
                iterador = iterador.proximo
            anterior.proximo = None
            return iterador

    def remove_first(self):
        if self.final is not None:
            self.inicial = self.inicial.proximo
