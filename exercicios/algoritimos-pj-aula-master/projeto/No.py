class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        self.anterior = None
        self.salto = None

    def __str__(self):
        if self.anterior is None and self.proximo is None:
            if self.salto is None:
                return f"Nó: |\t\t Nó: {self.dado} \t\t|"
            elif self.salto is not None:
                return f"Nó: |\t\t Nó: {self.dado} \t\t|\n -> |\t\t {self.salto.dado} \t\t|"
        elif self.anterior is None and self.proximo is not None:
            if self.salto is None:
                return f"Nó: |\t\t Nó: {self.dado} \t|\t Próximo: {self.proximo.dado} \t\t|"
            elif self.salto is not None:
                return f"Nó: |\t\t Nó: {self.dado} \t|\t Próximo: {self.proximo.dado} \t\t|\n " \
                       f"-> Salto: |\t\t {self.salto.dado} \t\t| "
        elif self.anterior is not None and self.proximo is None:
            if self.salto is None:
                return f"Nó: |\t\t Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t\t|"
            elif self.salto is not None:
                return f"Nó: |\t\t Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t\t|\n " \
                       f"-> Salto: |\t\t {self.salto.dado} \t\t|"
        elif self.anterior is not None and self.anterior is not None:
            if self.salto is None:
                return f"Nó: |\t\t Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t|" \
                       f"\t Próximo: {self.proximo.dado} \t\t|"
            elif self.salto is not None:
                return f"Nó: |\t\t Anterior: {self.anterior.dado} \t|\t Nó: {self.dado} \t|" \
                       f"\t Próximo: {self.proximo.dado} \t\t|\n" \
                       f"-> Salto: |\t\t {self.salto.dado} \t\t|"
