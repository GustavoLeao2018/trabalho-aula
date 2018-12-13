
menu = '''
== == == == == == == == == ==
MENU
== == == == == == == == == ==
0 - Finaliza
1 - Cadastro
2 - Relatório
Geral
3 - Relatório
Acima
da
Média
4 - Maiores
Salários
5 - Aumento
salarial
== == == == == == == == == ==
Escolha: '''

# declarar as listas.
listaNomes    = ["Ana","Carlos","Pedro"]
listaSalarios = [100,200,300]
listaSexo     = ['F','M','M']

while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        listaNomes.append(input("Digite seu nome: "))
        listaSalarios.append(input("Digite seu salario: "))
        listaSexo.append(input("Digite seu sexo: "))
    elif escolha == '2':
        # for é o laço
        # ind é a variável que controla o laço
        # range é o intervalo. Neste caso. de 0 até o tamanho da lista. incremento de 1

        for ind in range(0,len(listaNomes),1):
            print("[",listaNomes[ind],"], ", listaSalarios[ind],",",listaSexo[ind])

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
        nomeMaiorSalariosFEM = ""
        nomeMaiorSalariosMASC = ""

        for x in range(0,len(listaSalarios),1):
            if listaSalarios[x] > maiorSalarioMasculino and listaSexo[x] == 'M':
                maiorSalarioMasculino = listaSalarios[x]
                nomeMaiorSalariosMASC = listaNomes[x]

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

print("Fim.")