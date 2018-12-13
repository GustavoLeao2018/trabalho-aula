'''3. Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''
nome = "" # Declaração da variável
idade = 0
salario = 0

nome = input("Digite um nome: ")
while len(nome) <= 3:
    print("Digite um nome válido!")
    nome = input("Digite novamente um nome: ")
print("Seu nome: ", nome)

idade = int(input("Digite um idade: "))
while idade < 0 and idade > 150:
    print("Digite uma idade válido!")
    idade = int(input("Digite novamente um idade: "))
print("Sua idade: ", idade)

salario = float(input("Digite um salario: "))
while salario <= 0:
    print("Digite uma salario válido!")
    salario = float(input("Digite novamente um salario: "))
print("Sua salario: ", salario)

sexo = input("Digite um sexo: ").lower()[0]
while sexo != 'f' and sexo != 'm':
    print("Digite um sexo válido!")
    sexo = input("Digite novamente um sexo: ").lower()[0]
print("Seu sexo: ", sexo)


estado_civil = input("Digite um estado civil: ").lower()[0]
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print("Digite um estado civil válido!")
    estado_civil = input("Digite novamente um estado civil: ").lower()[0]
print("Seu estado civil: ", estado_civil)