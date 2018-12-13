"""Implementacao dos testes do Starfield."""

from behave import given, when, then

from starfield import cria_estrela, move_estrela


@given('dois valores inteiros e positivos, 0 e 600')
def given_limites_verticais_da_estrela(context):
    """Define limites verticais."""
    context.limites = (0, 600)


@given('uma lista com os valores 1, 2 e 3')
def given_lista_de_velocidades_validas(context):
    """Define a lista de velocidades validas."""
    context.velocidades = [1, 2, 3]


@when('eu crio um objeto que representa uma estrela')
def when_cria_estrela(context):
    """Cria estrela."""
    limites = context.limites
    velocidades = context.velocidades
    context.resultado = cria_estrela(limites, velocidades)


@then('a coordenada X da estrela é 800')
def then_coordenada_X_valida(context):
    """Verifica se coordenada X esta correta."""
    estrela = context.resultado
    esperado = 800
    observado = estrela[0]
    assert esperado == observado


@then('a coordenada Y da estrela esta entre 0 e 600')
def then_coordenada_Y_valida(context):
    """Verifica se coordenada Y esta correta."""
    estrela = context.resultado
    minimo, maximo = 0, 600
    observado = estrela[1]
    assert (minimo <= observado <= maximo) is True


@then('a velocidade da estrela é 1, 2 ou 3')
def then_velocidade_valida(context):
    """Verifica se a velocidade e valida."""
    estrela = context.resultado
    esperado = [1, 2, 3]
    observado = estrela[2]
    assert observado in esperado


@given('um objeto representando uma estrela')
def given_estrela(context):
    """Cria uma estrela."""
    context.estrela = cria_estrela((0, 600), [1, 2, 3])


@when('eu movo a estrela')
def when_move_estrela(context):
    """Move estrela."""
    context.resultado = move_estrela(context.estrela)


@then('a coordenada X varia de acordo com a velocidade da estrela')
def then_X_alterou_corretamente(context):
    """Testa se a coordenada X foi alterada corretamente."""
    speed = context.estrela[2]
    x = context.estrela[0]
    esperado = x - speed
    observado = context.resultado[0]
    assert esperado == observado


@then(u'a coordenada Y da estrela não varia')
def then_Y_nao_varia(context):
    """Testa se a coordenada Y nao foi alterada."""
    esperado = context.estrela[1]
    observado = context.resultado[1]
    assert esperado == observado


@then('a velocidade da estrela não varia')
def then_velocidade_nao_varia(context):
    """Testa se a velocidae nao foi alterada."""
    esperado = context.estrela[2]
    observado = context.resultado[2]
    assert esperado == observado
