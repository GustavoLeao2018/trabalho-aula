'''
Faça um programa que leia uma data de nascimento no formato de dd/mm/aaaa e
imprima a data com mes e e escrito por extenso
EXEMPLO:
Data = 20/02/2000
Resultado gerado
voçe nasceu em 20 de fevereiro de 2000
'''

data = input("Digite a data dd/mm/aaaa: ")
dia = data[:2]
mes = int(data[3:5]) - 1
ano = data[6:]


meses = ["janeiro", "fevereiro", "março", "abriu", "maio",
         "junho", "julho", "agosto", "setembro", "outubro",
         "novembro", "dezembro"]

for contador, item in enumerate(meses):
    if mes == contador:
        mes = item

print(f"Você nasceu dia: {dia} de {mes} de {ano}")
