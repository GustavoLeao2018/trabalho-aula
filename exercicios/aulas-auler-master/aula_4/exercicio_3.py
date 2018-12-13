"""
Faça
uma função que receba esta lista e utilizando as funções abaixo, determina e mostra quantos alunos com
mais de 13 anos possuem altura inferior à média de altura desses alunos.

a) Faça a função MediaTurma (lista) que recebe a lista com idade e altura de cada um dos aluno e retorna a
média de altura da turma

b) Faça a função Conta_Baixinhos (lista, media), que recebe a lista com idade e altura de cada um dos alunos e a
média de altura da turma, retornando quantos alunos com mais de 13 anos estão abaixo da média de altura da
turm

"""
from random import random, randint


def media_turma(idades, alturas):
    media = 0
    for altura in alturas:
        media += altura
    media /= len(idades)
    return media


"""
TODO: Crie a função calcula a média de altura dos alunos que tem idade menor que 13
"""


listaluno = []
idadeAluno = []
alturaluno = []
for l in range(10):
    listaluno.append("dhlkjshajdsahkjdsahkjsad")# input("digite nome do aluno")
    idadeAluno.append(randint(0, 100)) # int(input("digite a idade do aluno"))
    alturaluno.append(random() * 100) # float(input("digite a altura do aluno"))


for nome in listaluno:
    print(nome)

for idade in idadeAluno:
    print(idade)

for altura in alturaluno:
    print(altura)


lista_idade = []
lista_altura = []
for indice, idade in enumerate(idadeAluno):
    if int(idade) > 13:
        lista_idade.append(idade)
        lista_altura.append(alturaluno[indice])

print(f"Média da turma: {media_turma(lista_idade, lista_altura)}")
