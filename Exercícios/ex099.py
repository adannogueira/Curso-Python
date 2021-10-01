# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros. Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior.

import sys

def maior(lst):
	print(max(lst))

if __name__ == '__main__':
	try:
		n = [int(item) for item in sys.argv[1:]]
		maior(n)
	except ValueError:
		print('Só números inteiros são aceitos')
