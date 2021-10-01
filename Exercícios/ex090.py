# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
# o conteúdo da estrutura na tela.

aluno = {'Nome' : str(input('Nome: ')), 'Média' : float(input('Média: '))}
if aluno.get('Média') >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print(aluno)