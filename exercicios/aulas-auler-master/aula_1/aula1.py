# criei uma variável contendo o valor de true(verdadeiro)
continua = True

# loop vai continuar enquanto a variavel continua for igual a true(verdadeiro)
while continua == True:
    # atribui dentro da variável texto o valor de um texto digitado pelo usuário
    texto = input("Digite um texto:")
    # comparações
    # comparar se texto for igual a fim
    if texto == "fim":
        # continuar recebe falso
        continua = False
        # para o loop
    # tamanho do meu texto é menor que cinco
    elif len(texto) < 5:
        # impŕimir na tela o texto dentro das aspas
        print("Digite um valor válido!")
        # continuar o loop, pois foi atribuido a variavel continua o valor de verdadeiro(true)
        continua = True
    # senão, se tudo acima der errado
    else:
        # quantidade de caracterees e salva na variável quantidade
        quantidade = len(texto)
        # imprimo  ne tela o texto entre aspas
        print(f"A quantidade de caracteres é {quantidade}")

        # criar uma variável contador recebendo 0
        contador = 0
        # criar um loop para verificar caracter por caracter
        # carcter por caracter salvar dentro da variável letra
        for letra in texto:
            # comprarar para saber se é uma vogal
            if letra == "a" or letra == "e" or letra == "i" or letra == "u":
                #  acrescentar dentro do contador mais 1
                contador += 1

        # imprimir o texto abaixo
        print(f"A quantidade de vogais é {contador}")

        # loop continua
        continua = True