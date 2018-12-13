#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Teste de memoria. """

from timeit import timeit

print(timeit("L.append(0)", setup="L = []", number=100000))

print(timeit("L.insert(0,0)", setup="L = []", number=100000))
