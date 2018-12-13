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
mes = data[3:5]
ano = data[6:]


if mes == "01":
    mes = "janeiro"
elif mes == "02":
    mes = "fevereiro"
elif mes == "03":
    mes = "março"
elif mes == "04":
    mes = "abriu"
elif mes == "05":
    mes = "maio"
elif mes == "06":
    mes = "junho"
elif mes == "07":
    mes = "julho"
elif mes == "08":
    mes = "agosto"
elif mes == "09":
    mes = "setembro"
elif mes == "10":
    mes = "outubro"
elif mes == "11":
    mes = "novembro"
elif mes == "12":
    mes = "desembro"

print(f"Você nasceu dia: {dia} de {mes} de {ano}")
