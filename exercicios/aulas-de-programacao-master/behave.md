# Criando testes com o Behave resumidamente
1. Criar a pasta do projeto
2. Inicializar com o git
3. Criar a pasta de **features**.
4. Criar a pasta de **steps**.
5. Criar o arquivo da feature **teste.feature**.
6. Executar o `behave`.
7. Copiar o texto da resposta do código do **behave**.
8. Colar no arquivo de steps **steps.py**.
9. Inserir o **env3**, o **enc**, importar do **behave** o **given**, **when** e **then**.
10. Substituir o nome de cada método e dentro de acada um trocar o código por no método:
    * **Given:** criação de variável.
    * **When:**  chamado do método que será testado.
    * **Then:** verificação do teste em si.
11. É criado o arquivo que será testado, com o método que será importado, (e que deve ser importado em **steps**).
12. É executado o `behave` novamente.  
13. É executado o `git add`, o `git commit`, o `git remote add` e o `git push`.

# Criando testes com Behave por completo
1. Criar a pasta onde será criado o projeto (chame de **projeto**).
2. Inicializar com o git o repositório.
```bash
git init
```
3. Criar a pasta **features** para criar os testes com o ***gherkin***.
4. Criar a pasta **steps** para criar os testes em ***python***.
5. Criar o arquivo de teste dentro da pasta de **features**, chamado **teste.feature**, onde tera o código como o abaixo baixo:
```gherkin
# language: pt

Funcionalidade: calcular a média de dois números.
  Cenario: calcular a média.
  Dados os números 3 e 5,
  Quando calcular a média
  Entao o resultado é 4.
```
6. Executar o comando:
```bash
behave
```
Ou caso não funcione teste:
```bash
python -m behave
```
7. Será gerado os erros e os códigos no terminal dizendo:

**You can implement step definitions for undefined steps with these snippets:**

Com os códigos abaixo:
```python
@given(u'os números 3 e 5,')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given os números 3 e 5,')

@when(u'calcular a média')
def step_impl(context):
    raise NotImplementedError(u'STEP: When calcular a média')

@then(u'o resultado é 4.')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o resultado é 4.')
```
8. Criar o arquivo **steps.py** dentro do diretório ***steps***.

9. Copie o código anterior para o arquivo **steps.py**.

10. Importe do módulo **behave** os módulos:
  * given
  * then
  * when

Ficando:
```python
from behave import given, then, when
```
11. Adicionar o **env3** e o **enc**, para seguir as regras básicas do Python 3:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

12. Subistitua os nomes dos métodos como por exemplo:
  * Given:
```python
@given(u'os números 3 e 5,')
def step_given_two_numbers(context):
    raise NotImplementedError(u'STEP: Given os números 3 e 5,')
```
  * When
```python
@when(u'calcular a média')
def step_when_calculate_media(context):
    raise NotImplementedError(u'STEP: When calcular a média')
```
  * Then
```python
@then(u'o resultado é 4.')
def step_then_result_is_4(context):
    raise NotImplementedError(u'STEP: Then o resultado é 4.')
```

13. No método **given**, insira na variável global (**context**) as variáveis de **numero1** e **numero2**, ficando:
```python
@given(u'os números 3 e 5,')
def step_given_two_numbers(context):
    context.numero1 = 3
    context.numero2 = 5
```
14. No método **when**, insira na viariável global (**global**) a variável de **resposta** e dentro dela chamamos o método `media` com os números (**numero1**, **numero2**), como no código abaixo:
```python
@when(u'calcular a média')
def step_when_calculate_media(context):
    context.resposta = media(context.numero1, context.numero2)
```
15. Insira após a importação do behave, do módulo **media** (que é o arquivo **media.py**), o método `media`, ficando:
```python
from media import media
```
16. No método **then** insira o código de teste e compare se o valor da variável **resposta** é igual a 4, como abaixo:
```python
@then(u'o resultado é 4.')
def step_then_result_is_4(context):
    assert context.resposta == 4
```
17. Agora na pasta anterior a **features**, ou seja, na pasta **projeto**, crie o arquivo **media.py** e insira o **env3**, o **enc** e o método qua calcula a média ficando:
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def media(numero1, numero2):
    return (numero1 + numero2) / 2
```
18. Execute o comando do `behave` como abaixo:
```bash
behave
```
Ou também pode ser:
```bash
python -m behave
```
> Tem que ser mostrado a mensagem como abaixo:
> 1 feature passed, 0 failed, 0 skipped
> 1 scenario passed, 0 failed, 0 skipped
> 3 steps passed, 0 failed, 0 skipped, 0

19. Adicione os arquivos ao git, com o comando:
```bash
git add .
```

20. Comite com o comando:
```bash
git commit -m "Calculo de média e teste criado."
```

21. Vincule ao repositório na internet com o comando:
```bash
git remote add origin https://github.com/Seu_Usuario/nome_do_repositorio.git
```
22. De um `push` como abaixo:
```bash
git push -u origin master
```
