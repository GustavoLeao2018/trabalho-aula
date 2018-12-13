from Lista import Lista
from random import randint

lista = Lista()

for contador in range(101):
    lista.append(contador)

# print(lista)


print(lista.pop())


for i in range(randint(10, 100)):
    print("\n")
    lista.search(randint(0, 100))
    print("\n")

# print(lista)