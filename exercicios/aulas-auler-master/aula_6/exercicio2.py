
menu = '''
====================
MENU
====================
0- Finaliza
1- Cadastro
2- Relatório Geral
3- Relatório Acima da Média
4- Maiores Salários
5- Aumento salarial
6- Idade do Mais Velho
7- data de nascimento
====================
Escolha: '''

# declarar as listas.
listaNomes    = ["Ana","Carlos","Pedro"]
listaSalarios = [100,200,300]
listaSexo     = ['F','M','M']
listaIdade = [13,25,78,]
listameses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outulbro','novembro','dezembro']

while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        listaNomes.append(input("Digite seu nome: "))
        listaSalarios.append(float(input("Digite seu salario: ")))
        listaSexo.append(input("Digite seu sexo: "))
        listaIdade.append(int(input("Digite a idade: ")))
    elif escolha == '2':
        for indice, nome in enumerate(listaNomes):
            print("=-" * 100)
            print(f"Indice: {indice}", end=" \t|\t ")
            print(f"Nome: {nome}", end=" \t|\t ")
            print(f"Salário: {listaSalarios[indice]}", end=" \t|\t ")
            print(f"Sexo: {listaSexo[indice]}", end=" \t|\t ")
            print(f"Idade: {listaIdade[indice]}", end=" \t|\t ")
            print()
            print("=-"*100)

        # for é o laço
        # ind é a variável que controla o laço
        # range é o intervalo. Neste caso. de 0 até o tamanho da lista. incremento de 1

        # for ind in range(0,len(listaNomes),1):
        #     print("[",listaNomes[ind],"], ", listaSalarios[ind],",",listaSexo[ind])
        #     print(listaIdade)
        #     print(idadeMaisVelho)
        #     print(nomeMaisVelho)
        #     print(listameses[ind])
        # desta forma imprime as listas individualmente
        #print(listaNomes)
        #print(listaSalarios)
        #print(listaSexo)
    elif escolha == '3':
        # calcular a média
        soma = 0
        for salario in listaSalarios:
            soma = soma + float(salario)
        media = soma / len(listaSalarios)

        #quem ganha acima da média
        for x in range(0,len(listaNomes),1):
            if float(listaSalarios[x]) > media:
                print(listaNomes[x],", ",listaSalarios[x])


    elif escolha == '4':
        maiorSalarioMasculino = 0
        maiorSalarioFEMININO = 0
        nomeMaiorSalarioFEM = ""
        nomeMaiorSalarioMASC = ""

        for x in range(0,len(listaSalarios),1):
            if listaSalarios[x] > maiorSalarioMasculino and listaSexo[x] == 'M':
                maiorSalarioMasculino = listaSalarios[x]
                nomeMaiorSalariosMASC = listaNomes[x]

        maiorSalarioFEMININO = 0
        for x in range(0,len(listaSalarios),1):
            if listaSalarios[x] > maiorSalarioFEMININO and listaSexo[x] == 'F':
                maiorSalarioFEMININO = listaSalarios[x]
                nomeMaiorSalariosFEM = listaNomes[x]

        print(nomeMaiorSalariosMASC, maiorSalarioMasculino)
        print(nomeMaiorSalariosFEM , maiorSalarioFEMININO)


        if maiorSalarioMasculino > maiorSalarioFEMININO:
            dif = maiorSalarioMasculino - maiorSalarioFEMININO
        else:
            dif = maiorSalarioFEMININO - maiorSalarioMasculino

        print("Diferença = ",dif)


    elif escolha == '5':
        perc = int(input("Digite o percentual de aumento: "))

        soma = 0
        for salario in listaSalarios:
            soma = soma + float(salario)
        media = soma / len(listaSalarios)

        for x in range(0,len(listaSalarios),1):
            if listaSalarios[x] < float(media):
               listaSalarios[x] = listaSalarios[x] + (listaSalarios[x]*perc/100)



    elif escolha == '6':
        idade_maior = 0
        indice_maior = 0
        for indice, idade in enumerate(listaIdade):
            if indice == 0:
                idade_maior = idade
                indice_maior = indice
            if idade > idade_maior:
                idade_maior = idade
                indice_maior = indice

        print("Pessoa mais velha:")
        print(f"\t Nome: {listaNomes[indice_maior]}", end=" \t|\t ")
        print(f"\t Idade: {listaIdade[indice_maior]}")
        # print(f"\t Idade: {idade_maior}")

        # tamanhoLaço = 3
         # primeiraVez = True
         # idadeMaisVelho = 0
         #
         # for ind in range(0,len(listaNomes),1):
         #    nome = input("Digite o nome: ")
         #    idade= int(input("Digite a idade: "))
         #
         #    if primeiraVez: # identifica a primeira digitação
         #       nomeMaisVelho = nome
         #       idadeMaisVelho= idade
         #
         #    if idade > idadeMaisVelho:
         #       nomeMaisVelho = nome
         #       idadeMaisVelho= idade

            # print("A pessoa com mais idade é ",nomeMaisVelho)
            # print(" e sua idade é ",idadeMaisVelho)
    elif escolha == '7':
          #
          #
          # for x in range(0,len(listameses),1):
          dia, mes, ano = input('Data (dd/mm/aaaa): ').split('/')
          print('voce nasceu em:')
          print(f"{dia} de {listameses[int(mes) - 1]} de {ano}")
print("Fim.")


