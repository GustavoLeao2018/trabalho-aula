from projeto.No import No


class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None

    def anterior(self, valor):
        if valor < self.final.dado:
            return True
        else:
            return False

    def append(self, valor):
        if self.inicial is None and self.final is None:
            self.inicial = self.final = No(valor)
        elif self.anterior(valor) is False:
            self.final.proximo = no = No(valor)
            no.anterior = self.final
            self.final = self.final.proximo
        elif self.anterior(valor) is True:
            proximo = self.final.anterior
            print(f"Anterior: {proximo}")
            self.final.anterior = no = No(valor)
            print(f"Anterior novo: {self.final.anterior}")
            self.final = self.final.anterior
            print(f"Próximo: {self.final.proximo}")



    def __str__(self):
        iterador = self.inicial
        texto = "=-" * 20 + "[Lista:]" + "=-" * 20 + "\n"
        while iterador is not None:
            texto += str(iterador) + "\n"
            iterador = iterador.proximo
        texto += "=-" * 20 + "=-" + "=-" * 3 + "=-" * 20
        return texto
