# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*args, sit=False):
	lst = [arg for arg in args]
	dic = {'total': len(lst), 'maior': max(lst), 'menor': min(lst)}
	média = 0
	for n in lst:
		média += n
	média /= dic.get('total')
	dic['media'] = média
	if sit:
		if média >= 7:
			dic['situação'] = 'BOA'
		elif 5 < média < 7:
			dic['situação'] = 'REGULAR'
		else:
			dic['situação'] = 'RUIM'
	return dic


if __name__ == '__main__':
	print(notas(3,2,1.8,7, sit=True))
	print(notas(5,2,8,7, sit=True))
	print(notas(10,8,5,7, sit=True))
	print(notas(3,2,1.8,7))