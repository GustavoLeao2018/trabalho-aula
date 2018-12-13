menu = """
====================
MENU
====================
0- Finaliza
1- Cadastro
2- Relatório Geral
3- Alteração de Dados
4- Exclusão
5- Relatório por sexo
====================
Consistência:
Escolha: 
"""
listaNome = []
listaIdade = []
listaSexo = []
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        for i in range(3):
            nome = input("digite um nome")
            listaNome.append(nome)
            idade = input("digite a idade")
            listaIdade.append(idade)
            sexo = input("digite o sexo")
            while sexo != 'f' and sexo != 'm':
                sexo = input("digite o sexo")
            listaSexo.append(sexo)
    elif escolha == '2':
        for nome in listaNome:
            print(nome)

        for idade in listaIdade:
            print(idade)

        for sexo in listaSexo:
            print(sexo)

    elif escolha == '3':
        pesquisa = input("altere um nome")
        #for nome in listaNome:
        #    if pesquisa == nome:
        # listaNome[listaNome.index(pesquisa)] = input("Digite um outro nome:")

        for indice, nome in enumerate(listaNome):
            if pesquisa == nome:
                listaNome[indice] = input("Digite um outro nome:")

    elif escolha == '4':
        pesquisa = input("digite um nome")
        # for nome in listaNome:
        #   if pesquisa == nome:
        listaNome.remove(pesquisa)

    elif escolha == '5':
        pesquisa = input("digite o sexo")

        for sexo in listaSexo:
            if sexo == pesquisa:
                print(sexo)


