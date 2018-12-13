#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from behave import given, then, when
from mediano import mediano


@given(u'os números 3, 4, 5')
def step_given(context):
    context.num1 = 3
    context.num2 = 4
    context.num3 = 5


@when(u'verificado')
def step_when(context):
    context.resp = mediano(context.num1, context.num2, context.num3)


@then(u'o mediano é 4.')
def step_then(context):
    assert context.resp == 4
