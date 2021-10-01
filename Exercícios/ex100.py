# Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.
from random import randint

def sorteia():
	return [randint(0, 100) for n in range(5)]


def somaPar(lst):
	soma = 0
	for n in lst:
		soma += n
	return soma


if __name__ == '__main__':
	numeros = sorteia()
	print(f'Números sorteados: {numeros}')
	print(f'Valor da soma entre eles: {somaPar(numeros)}')