# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
# do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome, gols):
	return f'O jogador {nome or "<desconhecido>"} fez {gols or "0"} gol(s) no campeonato.'

if __name__ == '__main__':
	print(ficha(input('Digite o nome do jogador: '), input('Número de gols: ')))
