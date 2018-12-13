from No import No

class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None
        self.contador = 0

    def __len__(self):
        return self.contador

    def append(self, valor):
        if self.inicial is None and self.final is None:
            """
            no = No(valor)
            self.inicial = no
            self.final = no
            """
            self.inicial = self.final = No(valor)
        else:
            # final aponta para o novo nó (Próximo final)
            self.final.proximo = no = No(valor)
            no.anterior = self.final
            self.final = self.final.proximo
        self.contador += 1

    def add_first(self, valor):
        no = No(valor)
        no.proximo = self.inicial
        self.inicial = no

        proximo = self.inicial.proximo
        proximo.anterior = no
        self.contador += 1

    def pesquisa(self, valor):
        iterador = self.inicial
        cont = 0
        while iterador is not None:
            if (cont % 5) == 0:
                print(iterador)
            cont += 1
            iterador = iterador.proximo


    def __str__(self):
        iterador = self.inicial
        texto = "Lista: \n"
        while iterador is not None:
            texto += str(iterador)+"\n"
            iterador = iterador.proximo
        return texto
