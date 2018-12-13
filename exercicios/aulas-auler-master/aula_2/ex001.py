"""
Faça um programa que peça uma nota, entre zero e dez excluindo os dois.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

nota = int(input("Digite uma nota:"))

while nota >= 10 or nota <= 0:
    print(f"O número {nota}, é invalido!")
    print("Digite um número entre 0 e 10!")
    nota = int(input("Digite uma nota:"))

"""

q | w | resultado
v | f | f
f | v | f
v | v | v
f | f | f

"""