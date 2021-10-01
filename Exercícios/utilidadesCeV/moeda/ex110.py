# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
# que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado
# até aqui.
import sys, os
sys.path.append('E:/Adan/OneDrive/Cursoemvideo/Exercícios/utilidadesCeV/moeda')
import ex108
import moeda


def resumo(valor):
	print(f'Resumo do valor:\t R$ {ex108.moeda(valor):>8}')
	print('------------------------------------')
	print(f'Dobro do valor:\t\t R$ {ex108.moeda(moeda.dobro(valor)):>8}')
	print(f'Metade do valor:\t R$ {ex108.moeda(moeda.metade(valor)):>8}')
	print(f'20% de aumento:\t\t R$ {ex108.moeda(moeda.aumentar(valor, 20)):>8}')
	print(f'10% de desconto:\t R$ {ex108.moeda(moeda.diminuir(valor, 10)):>8}')