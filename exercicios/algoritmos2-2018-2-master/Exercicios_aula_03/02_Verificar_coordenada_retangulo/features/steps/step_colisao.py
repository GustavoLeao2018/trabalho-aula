"""Testa colisao de objetos."""

from behave import given, when, then

from retangulo import Retangulo


@given('um ponto com as coordenadas ({x}, {y})')
def given_ponto(context, x, y):
    """Dado um ponto."""
    context.ponto = (int(x), int(y))


@given('um retângulo nas coordenadas ({x:d}, {y:d}) e dimensão ({w:d}, {h:d})')
def given_retangulo(context, x, y, w, h):
    """Cria retangulo."""
    context.retangulo = Retangulo(x, y, w, h)


@when('quero saber se o ponto está dentro do retangulo')
def when_testa_colisao_ponto(context):
    """Invoca teste de colisao."""
    context.resultado = context.retangulo.colide(context.ponto)


@then('o resultado é "{esperado}".')
def then_objetos_colidem(context, esperado):
    """Verifica de colisao foi a esperada."""
    booleano = True if esperado == 'verdadeiro' else False
    assert context.resultado is booleano
