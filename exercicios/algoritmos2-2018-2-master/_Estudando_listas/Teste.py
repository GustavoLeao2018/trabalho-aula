from Lista import Lista

lista = Lista()
for i in range(1,11):
    lista.append(i)

lista.add_first(5)

print(lista)

lista.pesquisa(4)
