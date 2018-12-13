"""Cria um campo de estrelas."""

from random import randint, choice


def cria_estrela(limites, velocidades):
    """Cria uma estrela com os parametros dados."""
    x = 800
    y = randint(*limites)
    speed = choice(velocidades)
    return (x, y, speed)


def move_estrela(estrela):
    """Move uma estrela."""
    x, y, speed = estrela
    return (x - speed, y, speed)
