# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
med = float((n1+n2)/2)

print(f'Suas notas são \033[33m{n1:.1f}\033[m e \033[33m{n2:.1f}\033[m, e sua nota média é \033[33m{med:.1f}\033[m.')

if med >= 7:
    print('Parabéns!')
else:
    print('Estude mais!!')
