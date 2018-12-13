class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None

    def __str__(self):
        if self.proximo is None:
            return f"Nó: {self.dado} | \tPróximo Nó: {self.proximo} \n"
        else:
            return f"Nó: {self.dado} | \tProximo Nó: {self.proximo.dado} \n"

class Lista:
    def __init__(self):
        self.inicial = None
        self.final = None
        self.tamanho = 0

    def last(self):
        return self.final

    def first(self):
        return  self.inicial

    def size(self):
        return self.tamanho

    def __len__(self):
        return  self.size()


    def append(self, valor):
        if self.final is None:
            self.inicial = self.final = No(valor)
        else:
            self.final.proximo = No(valor)
            self.final = self.final.proximo

    def addFirst(self, valor):
        no = No(valor)
        no.proximo = self.inicial
        self.inicial = no

    def removeFirst(self):
        self.inicial = self.inicial.proximo

    def removeLast(self):
        anterior = None
        iterador = self.inicial
        while iterador.proximo:
            if iterador.proximo is None:
                break
            anterior = iterador
            iterador = iterador.proximo
        anterior.proximo = None

    def pop(self):
        anterior = None
        iterador = self.inicial
        while iterador.proximo:
            if iterador.proximo is None:
                break
            anterior = iterador
            iterador = iterador.proximo
        anterior.proximo = None
        return iterador

    def remove(self, valor):
        iterador = self.inicial
        while iterador.proximo:
            if iterador.dado is valor:
                anterior.proximo = iterador.proximo
            anterior = iterador
            iterador = iterador.proximo

        if self.final.dado is valor:
            self.pop()
        elif self.inicial.dado is valor:
            self.removeFirst()

    def __str__(self):
        texto = ""
        iterador = self.inicial
        while iterador is not  None:
            texto += str(iterador)
            iterador = iterador.proximo
        return texto




if __name__ == '__main__':
    from random import  randint

    lista = Lista()

    for i in range(30):
        lista.append(randint(0, 10))

    print(str(lista))
    
    print("="*100)

    n = randint(0, 10)
    print(n)
    lista.remove(n)

    print(str(lista))