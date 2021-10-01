# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
# se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

def voto(nascimento):
	idade = date.today().year - nascimento
	if idade < 16:
		return 'NEGADO'
	elif 18 <= idade <= 65:
		return 'OBRIGATÓRIO'
	else:
		return 'OPCIONAL'


if __name__ == '__main__':
	print(f'No seu caso o voto é: {voto(int(input("Digite seu ano de nascimento: ")))}')

