# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
# mantenha tudo funcionando.


def aumentar(valor, percentual=0):
	return ((percentual / 100) + 1) * valor


def diminuir(valor, percentual=0):
	return (1 - (percentual / 100)) * valor


def dobro(valor):
	return valor * 2


def metade(valor):
	return valor / 2


def moeda(valor):
	return f'{valor:.2f}'.replace('.', ',')


def passar(valor):
	return valor


def resumo(valor):
	print(f'Resumo do valor:\t R$ {moeda(valor):>8}')
	print('------------------------------------')
	print(f'Dobro do valor:\t\t R$ {moeda(dobro(valor)):>8}')
	print(f'Metade do valor:\t R$ {moeda(metade(valor)):>8}')
	print(f'20% de aumento:\t\t R$ {moeda(aumentar(valor, 20)):>8}')
	print(f'10% de desconto:\t R$ {moeda(diminuir(valor, 10)):>8}')