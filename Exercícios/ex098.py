# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def contador(início, fim, passo):
	if passo == 0:
		passo = 1
	if início < fim and passo < 0:
		passo *= (-1)
	elif início > fim and passo > 0:
		passo *= (-1)
	conta = [i for i in range(início, fim, passo)]

	print('Contando: ', end='')
	sleep(1)
	for n in range(1, 11):
		print(n, end=', ', flush=True)
		sleep(1)
	print('acabei!')
	sleep(1)
	print('Contando: ', end='')
	sleep(1)
	for n in range(10, -1, -2):
		print(n, end=', ', flush=True)
		sleep(1)
	print('acabei!')
	sleep(1)
	print('Contando: ', end='')
	sleep(1)
	for n in conta:
		print(n, end=', ', flush=True)
		sleep(1)
	print('acabei!')


if __name__ == '__main__':
	contador(int(input('Digite o início: ')),
		int(input('Digite o fim: ')),
		int(input('Digite o passo: ')))