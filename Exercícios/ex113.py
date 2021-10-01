# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.

def leiaInt(numero):
	'''
	-> Função validadora de números, só aceita inteiros como input.
	param numero: valor a ser validado
	return: número inteiro
	'''
	while 1:
		try:
			return int(numero)
		except ValueError:
			print('\033[7mDigite um número inteiro válido.\033[m')
			numero = input('Digite um número: ')


def leiaFloat(numero):
	'''
	-> Função validadora de números, só aceita inteiros e floats como input.
	param numero: valor a ser validado
	return: número float
	'''
	while 1:
		try:
			return float(numero)
		except ValueError:
			print('\033[7mDigite um número inteiro válido.\033[m')
			numero = input('Digite um número: ')


if __name__ == '__main__':
	print(f'Você digitou o número {leiaInt(input("Digite um número inteiro: "))}')
	print(f'Você digitou o número {leiaFloat(input("Digite um número float: "))}')