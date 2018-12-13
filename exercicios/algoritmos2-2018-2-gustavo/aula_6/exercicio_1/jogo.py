from pygame import *
from sys import exit

class Main:
    def criar_janela(self):
        while True:
            for evento in event.get():
                if evento.type == QUIT:
                    exit()
                if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                    exit()

            display.flip()

    def __init__(self):
        init()

        self.tamanho = self.largura, self.altura = 800, 600

        self.janela = display.set_mode(self.tamanho)
        display.set_caption("Jogo base criado!")

        self.criar_janela()




if __name__ == '__main__':
    Main()