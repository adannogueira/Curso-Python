# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from utilidadesCeV.moeda import *
from utilidadesCeV.dado import *


while 1:
	valor = leiaDinheiro('Digite o preço: R$')
	if input('Deseja o resumo? [S/N] ')[0].lower() == 's':
		resumo(valor)
		break
	percentual = float(input('Digite o percentual: % '))
	formatar = input('Deseja o valor formatado? [S/N] ')[0].lower()
	if formatar == 's':
		formatar = moeda
	else:
		formatar = passar
	print(f'Aumentando {percentual}% temos R$ {formatar(aumentar(valor, percentual))}')
	print(f'Diminuindo {percentual}% temos R$ {formatar(diminuir(valor, percentual))}')
	print(f'O dobro de R$ {formatar(valor)} é R$ {formatar(dobro(valor))}')
	print(f'A metade de R$ {formatar(valor)} é R$ {formatar(metade(valor))}')
	break
