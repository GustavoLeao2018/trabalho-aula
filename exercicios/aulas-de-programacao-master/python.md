# Comandos básicos Python
# Impimir
## Imprimindo na tela
Para imprimir na tela um texto simples:
```python
print("Este texto será mostrado na tela!")
```
## Para imprimir uma variável
Para imprimir uma variável temos algumas maneiras:
1. Somente a variável:
```python
nome = "Gustavo"
print(nome)
```
2. Usando **,** (concatenando):
```python
nome = "Gustavo"
print("Olá",nome,"tudo bem?")
```
3. Usando o format:
```python
nome = "Gustavo"
idade = 21
print("{} tem {} anos.".format(nome, idade))
```
> Este vai trocar respectivamente cada **{}** por as variáveis que estão no format.
4. Usando dicionários
```python
dicionario = {
  "nome" : "Gustavo",
  "idade" : 21
}
print("{nome} tem {idade} anos.".format(**dicionario))
```
> Neste caso temos de colocar  dentro das chaves o nome da chave (que é a parte antes dos dois pontos -**:**) para que ele relacione com a chave do dicionario e coloque o valor no local.
> O ****dicionario** expande completamente não sendo necessário colocar no formato abaixo, (que funciona caso seja usado):
```python
print("{nome} tem {idade} anos.".format(nome=dicionario['nome'], idade=dicionario['idade']))
```
# Ler
## Ler apartir do teclado
Para lermos informações do teclado devemos digitar o comando:
```python
variavel = input("Digite algum valor:")
```
Onde temos uma variável que recebe um valor no formato de **string** e temos o texto a ser mostrado na tela dentro de aspas.

# Converter dados
## De String para int
```python
numero_inteiro = int("5")
```
> Podemos trocar o valor dentro dos parenteses por um `input` ficando:
```python
numero_inteiro = int(input("Digite um número inteiro:"))
```
## De String/Int para float
```python
numero_decimal = float("5.3")
# ou também pode ser
numero_decimal = float("5")
# ou também pode ser
numero_decimal = float(5)
```
> Também deve ser ressaltado que pode ser trocado esse valor por um input.

## De String/Int para bolean
```python
numero_decimal = bool("True")
# ou também pode ser
numero_decimal = bool(1)

```
## De Float/Int/Boolean para String
```python
texto_numero = str(5)
# ou também pode ser
texto_numero = str(5.3)
# ou também pode ser
texto_numero = str(True)
```

# Comparações
# Simples
Para comparações simples podemos fazer da seguinte maneira:
```python
numero = 3
numero = 2
numero = 1
maior = 0
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
print("O maior número é: {}".format(maior))
```
# Com uma variação
Para comparações com uma verificação e o oposto dessa faça o seguinte:
```python
numero = 3
numero = 2
numero = 1
maior = 0
if numero1 > numero2 and numero1 > numero3:
  maior = numero1
else:
  maior = 3
print("O maior número é: {}".format(maior))
```
# Comparações com mais de uma verificação
Para comparações mais complexas devemos ter o seguinte código:
```python
numero = 3
numero = 2
numero = 1
maior = 0
if numero1 > numero2 and numero1 > numero3:
  maior = numero1
elif numero2 > numero1 and numero2 > numero3:
  maior = numero2
else:
  maior = numero3
print("O maior número é: {}".format(maior))
```

> Em todos as verificações (exceto no `else` que não tem) podemos ter uma ou mais no formato de condições como as acima que utilizam os conectivos(operadores lógicos), listados na tabela:

| Operador | Funcionalidade |
|:--------:|:--------------:|
| and      | E              |
| or       | Ou             |


Tabela verdade (e)

| Q  | P | Resultado |
|:--:|:-:|:---------:|
| V  | V | V         |
| V  | F | F         |
| F  | V | F         |
| F  | F | F         |

Tabela verdade (ou)

| Q  | P | Resultado |
|:--:|:-:|:---------:|
| V  | V | V         |
| V  | F | V         |
| F  | V | V         |
| F  | F | F         |

> Toda comparação deve ser feita com os operadores relacionais que são:

| Operador | Funcionalidade   |
|:--------:|:----------------:|
| <        | Menor que        |
| >        | Maior que        |
| <=       | Menor ou igual a |
| >=       | Maior ou igual a |
| ==       | Igual a          |
| !=       | Diferente de     |

> Para os operadores de verdade ou falsidade, devemos comparar algo e dizermos sena comparação deverá ser igual(`==`) ou diferente(`!=`)

| Operador | Funcionalidade|
|:--------:|:-------------:|
| True     | Verdadeiro    |
| False    | Falso         |

# Calculos
Podemos calcular a soma, multiplicação, divisão, subtração, exponenciação, divisão inteira e modulo (resto) da divisão:

| Operador | Funcionalidade   |
|:--------:|:----------------:|
| +        | Soma             |
| -        | Subtração        |
| *        | Multiplicação    |
| /        | Divisão          |
| **       | Exponenciação    |
| //       | Divisão inteira  |
| %        | Resto da divisão |

Exemplo:
```python
numero1 = 5
numero2 = 3
media = (numero1 + numero2) / 2
```

# 
