from pygame import *
from sys import exit
from random import randint

class Main:
    def criar_janela(self):
        while True:
            for evento in event.get():
                if evento.type == QUIT:
                    exit()
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    exit()
            display.flip()

    def estrela(self):
        circulo = draw.circle(self.janela, self.branca, [randint(0, 800), randint(0, 600)], 1)
        return  circulo


    def __init__(self):
        init()

        self.tamanho = self.largura, self.altura = 800, 600
        self.branca = (255, 255, 255)

        self.janela = display.set_mode(self.tamanho)
        display.set_caption("Jogo base criado!")

        for i in range(randint(100, 2000)):
            self.estrela()

        self.criar_janela()


if __name__ == '__main__':
    Main()