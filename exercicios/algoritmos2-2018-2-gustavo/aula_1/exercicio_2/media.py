#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def media(numero1, numero2):
	"""Cria o método que calcula a média de dois valores."""
	return (numero1 + numero2) / 2

def maior_de_tres(n1, n2, n3):
	"""Método que verifica o maior de três números."""
	if n1 > n2 and n1 > n3:
		return n1
	elif n2 > n1 and n2 > n3:
		return n2
	else:
		return n3
