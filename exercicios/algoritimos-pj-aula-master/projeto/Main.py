from projeto.Lista import Lista
from random import randint

lista = Lista()

for cont in range(0, 101):
    lista.append(randint(0, 100))

print(lista)