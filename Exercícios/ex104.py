# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

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


if __name__ == '__main__':
	print(f'Você digitou o número {leiaInt(input("Digite um número: "))}')