from behave import given, when, then
from meio import maior_de_tres

@given(u'os números ({a:d}, {b:d}, {c:d})')
def step_impl(context, a, b, c):
    context.a = a
    context.b = b
    context.c = c


@when(u'verificar qual o maior')
def step_impl(context):
    a = context.a
    b = context.b
    c = context.c
    context.maior = maior_de_tres(a, b, c)


@then(u'o maior é {maior:d}')
def step_impl(context, maior):
    assert context.maior == maior

