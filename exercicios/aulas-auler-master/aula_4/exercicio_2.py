'''
Faça um programa que receba a temperatura média
de cada mês do ano e armazene-as em uma lista.
Em seguida, calcule a média anual das temperaturas
e mostre a média calculada juntamente com todas as
temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 –
Janeiro, 2 – Fevereiro, . . . ).
48
'''

from random import randint

meses = []
for mes in range(12):
    temperatura = randint(0, 50)
    meses.append(temperatura) # float(input('Digite a temperatura do mês: °'))
    print(f'Digite a temperatura do mês: °{temperatura}')

media_anual = 0
for mes in meses:
    media_anual += mes
media_anual /= 12
print(f"Média anual: {media_anual}")


mes_do_ano = ["janeiro", "fevereiro", "março", "abriu", "maio",
         "junho", "julho", "agosto", "setembro", "outubro",
         "novembro", "dezembro"]

indice = 0
for mes in meses:
    if mes > media_anual:
        print(f"Média mensal do mes {mes_do_ano[indice]}: {mes}")
    indice += 1


