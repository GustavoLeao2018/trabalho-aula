'''
Faça um algoritmo que utilize 3 listas. lista1, lista2 e lista3. Aceite apenas de números inteiros
nestas listas.
 Seu algoritmo deve ler vários números maiores que zero.
 Se o número lido for par ou estiver no intervalor entre 10 e 100(inclusive), este deverá
ser inserido na lista1.

 Se o número lido for impar ou estiver no intervalo entre 50 e 150(inclusive), este deverá
ser inserido na lista2.
 Se o número lido for maior que 0 e menor que 10, ou estiver no intervalo entre 40 e
120(inclusive) o número deverá ser inserido na lista3.
 O algoritmo encerra no momento em que for lido o número 0(zero).
 Caso o número lido seja negativo ou maior que 150, incremnte um contador de erros.
Quanto este contador chegar em 3, todas as listas deverão ter seus conteúdos
apagados e o contador inciado em zero novamente.

 Para cada número digitado imprima as 3 listas conforme o exemplo:
LISTA1 = [2],[4],[12],[8] [33] 55, 56
LISTA2 = [3],[33],[55],[56]
LISTA3 = [2],[3],[4],[8],[55],[56]


Ao finalizar anexe seu arquivo no blackboard.

'''


lista1 = []
lista2 = []
lista3 = []
contador = 0

while True:
    numero = int(input("Digite um número:"))
    while numero <= 0:
        numero = int(input("Digite outro número [maior que 0]:"))


    """
    se numero pelo resto da divisão for igual a zero ou numero for >= 10 e numero <= 100 então
        adicione a lista o número    
    """
    if (numero % 2) == 0 or numero >= 10 and numero <= 100:
        lista1.append(numero)
    if (numero % 2) != 0 or numero >= 50 and numero <= 150:
        lista2.append(numero)
    if numero > 0 and numero < 10 or numero >= 40 and numero <= 120:
        lista3.append(numero)
    if numero == 0:
        break
    if numero < 0 or numero > 150:
        contador += 1  # contador = contador + 1
        if contador == 3:
            lista1.clear()
            lista2.clear()
            lista3.clear()
            contador = 0

    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista 3: {lista3}")
    # continuar = input("Quer continuar? [s/n]").lower()[0]
    # if continuar == 'n':
    #     break



"""

lista1 = []
lista2 = []
lista3 = []
n = 0

if lista1 > 10:

    lista1.append(int(input("digite um numero")))

    print(n)

    if lista1 <= 100:

    lista1.append(int(input("digite um numero")))

    '''
  Faça um algoritmo que utilize 3 listas. lista1, lista2 e lista3. Aceite apenas de números inteiros
  nestas listas.
   Seu algoritmo deve ler vários números maiores que zero.
   Se o número lido for par ou estiver no intervalor entre 10 e 100(inclusive), este deverá
  ser inserido na lista1.
  
   Se o número lido for impar ou estiver no intervalo entre 50 e 150(inclusive), este deverá
  ser inserido na lista2.
   Se o número lido for maior que 0 e menor que 10, ou estiver no intervalo entre 40 e
  120(inclusive) o número deverá ser inserido na lista3.
   O algoritmo encerra no momento em que for lido o número 0(zero).
   Caso o número lido seja negativo ou maior que 150, incremnte um

"""