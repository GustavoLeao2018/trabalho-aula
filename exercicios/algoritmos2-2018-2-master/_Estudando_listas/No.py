class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        self.anterior = None
        self.salto = None

    def __str__(self):
        if self.anterior is None and self.proximo is None:
            return f"|\t Anterior: {self.anterior} \t|\t Nó: {self.dado} \t|\t Próximo: {self.proximo} \t|"
        elif self.proximo is not None and self.anterior is None:
            return f"Anterior: {self.anterior} Nó: {self.dado} Próximo: {self.proximo.dado}"
        elif self.anterior is not None and self.proximo is None:
            return f"Anterior: {self.anterior.dado} Nó: {self.dado} Próximo: {self.proximo}"
        else:
            return f"Anterior: {self.anterior.dado} Nó: {self.dado} Próximo: {self.proximo.dado}"
