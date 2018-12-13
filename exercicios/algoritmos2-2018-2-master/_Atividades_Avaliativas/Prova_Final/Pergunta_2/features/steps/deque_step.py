"""Comportamentos de um Deque."""

from behave import given, when, then
from Deque import Deque


@given(u'o tamanho da estrutura que é {tamanho:d}')
def _given_tamanho_da_estrutura(context, tamanho):
    context.tamanho = tamanho


@when(u'crio um deque')
def _when_crio_um_deque(context):
    context.deque = Deque(context.tamanho)


@then(u'tenho um deque com capacidade para armazenar {elementos:d} elementos')
def _then_tenho_um_deque_com_capacidade(context, elementos):
    assert context.deque.tamanho == elementos


@then(u'uma estrutura esta vazia')
def _then_estrutura_vazia(context):
    assert context.deque.empty is True


@given(u'que eu tenho um deque')
def _given_tenho_um_deque(context):
    context.deque = Deque(10)


@when(u'insiro, no final da estrutura, o valor {valor}')
def _step_impl(context, valor):
    context.deque.push_back(valor)


@then(u'a estrutura nao esta vazia')
def _then_estrutura_nao_esta_vazia(context):
    assert context.deque.empty is False


@then(u'o elemento na frente da estrutura tem o valor {valor}')
def _then_elemento_da_frente(context, valor):
    print(context.deque.peek_front().dado, valor)
    assert context.deque.peek_front().dado is valor


@when(u'insiro, no final da estrutura, os valores [ 1 , 2 , 3 , 4 ]')
def _when_insiro_no_final(context):
    lista_acrescentar = [1, 2, 3, 4]
    for item in lista_acrescentar:
        context.deque.push_back(item)


@then(u'o elemento no final da estrutura tem o valor {valor}')
def _then_elemento_final_tem_valor(context, valor):
    print(context.deque.peek_back().dado)
    assert context.deque.peek_back().dado is valor


@given(u'este deque tem elementos, inseridos no final, [ 1 , 3 , 5 , 7 ]')
def _given_deque_tem_elementos(context):
    lista_acrescentar = [1, 3, 5, 7]
    for item in lista_acrescentar:
        context.deque.push_back(item)
