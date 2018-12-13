#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Exercício 02 - aula Aula_4 (Listas). """


# 1 ) Leia dez números inseridos pelo usuário.
def ler_10_numeros():
    lista_numeros = []
    for item in range(3):
        numero = int(input("Digite um número: "))
        lista_numeros.append(numero)
    return lista_numeros


#  2) Qual o MAIOR número e qual o seu índice?
def maior_numero(lista_numeros):
    maior = max(lista_numeros)
    indice = lista_numeros.index(maior)
    # Aqui retorna um TUPLA populada com (maior) e (indice)
    return maior, indice


#  3) Qual o MENOR número e qual o seu índice?
def menor_numero(lista_numeros):
    menor = min(lista_numeros)
    indice = lista_numeros.index(menor)
    # Aqui retorna um TUPLA populada com (maior) e (indice)
    return menor, indice


# 4) Qual a soma dos números pares?
def soma_pares(lista_numeros):
    soma_dos_pares = 0
    for numero in lista_numeros:
        if (numero % 2) == 0:
            soma_dos_pares += numero
    return soma_dos_pares


# 5) Qual a soma dos números ímpares?
def soma_impares(lista_numeros):
    soma_dos_impares = 0
    for numero in lista_numeros:
        if (numero % 2) != 0:
            soma_dos_impares += numero
    return soma_dos_impares


# 6) Imprima os números na ordem inversa em que foram digitados.
# Retorna lista_numero INVERSA (não imprime nada)
def inverte_lista(lista_numeros):
    lista = []
    for numero in reversed(lista_numeros):
        lista.append(numero)
    return lista


#  Criando função para IMPRIMIR na tela
def imprime_lista(lista_numeros):
    for numero in lista_numeros:
        print(numero)


# Criando metodo para mostrar a lista
def mostra_lista(x):
    for numero in x:
        print(numero)


# Metodo para imprimir o MAIOR número e seu INDICE
def imprime_maior(maior_numero):
    numero, indice = maior_numero
    print("Maior número: [{}] | Índice: [{}]" .format(numero, indice))


# Imprime algo
def imprimir_algo(x):
    imprimir = x
    print(imprimir)


print("======== Testando: Ler 10 Números =========")
# Recebendo números
lista_p = ler_10_numeros()

# Imprime lista invertida
print("Lista inversa " + "="*50)
lista_invertida = inverte_lista(lista_p)
mostra_lista(lista_invertida)

# Imprime a soma dos números impares
soma = soma_impares(lista_p)
print("Soma dos números impares " + "="*50)
imprimir_algo(soma)

# Imprimir o MAIOR número da lista e seu INDICE
print("Maior número e seu índice " + "="*50)
maior = maior_numero(lista_p)
imprime_maior(maior)
