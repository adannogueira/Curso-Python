# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(valor, percentual=0):
	return ((percentual / 100) + 1) * valor


def diminuir(valor, percentual=0):
	return (1 - (percentual / 100)) * valor


def dobro(valor):
	return valor * 2


def metade(valor):
	return valor / 2

