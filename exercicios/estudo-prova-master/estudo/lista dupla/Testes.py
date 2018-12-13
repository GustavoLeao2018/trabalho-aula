from Lista import Lista
from random import randint

lista = Lista()
for i in range(10):
    lista.append(randint(0, 100))

print(lista)
lista.add_first(randint(0, 100))
print(lista)
print(lista.pop())
print(lista)
lista.remove_first()
print(lista)