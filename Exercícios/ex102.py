# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(numero, show=False):
	'''
	Função para fatorar um número natural.
	param numero: o número natural a ser fatorado
	param show: se definido como True, mostra as etapas de fatoração
	return: o resultado do fatorial
	'''

	if numero < 0:
		return 'Fatoração só admite números positivos'

	elif numero > 0:
		resultado = numero
		fatoração = []
		if numero == 1:
			fatoração.append(numero)
		else:
			fatoração = sorted([i for i in range(1, numero)], reverse=True)
		for n in fatoração:
			resultado *= n
		
		if show:
			fatorstring = str(numero)
			for v in fatoração:
				fatorstring = fatorstring + f' x {v}'
			fatorstring = fatorstring + f' = {resultado}'
			return fatorstring
		else:
			return resultado
	else:
		return '1'

if __name__ == '__main__':
	print(fatorial(1, True))
	print(fatorial(2))
	print(fatorial(-2))
	print(fatorial(5, True))