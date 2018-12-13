"""Implementa classe retangulo com tratamento de colisao."""


class Retangulo:
    """Define objeto retangulo."""

    def __init__(self, x, y, width, height):
        """Inicializa objeto retangulo com os parametros dados."""
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def colide(self, ponto):
        """Testa colisao do objeto com um ponto."""
        x, y = ponto
        if x < self.x or x > self.x + self.width:
            return False
        if y < self.y or y > self.y + self.height:
            return False
        return True
