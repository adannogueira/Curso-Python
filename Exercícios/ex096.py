# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def área(l, c):
	print(f'Área: {l * c}m²')

if __name__ == '__main__':
	print('Para cálculo da área do terreno, informe:')
	área(int(input('Largura: ')), int(input('Comprimento: ')))