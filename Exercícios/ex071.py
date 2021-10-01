# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('{:-^30}'.format('BANCO DO ZÉ'))
print('{:-^30}'.format('SisBZ Saque'))
valor = int(input('Valor a sacar: R$ '))

n50 = valor // 50
sobra1 = valor % 50
n20 = sobra1 // 20
sobra2 = sobra1 % 20
n10 = sobra2 // 10
n1 = sobra2 % 10

print('{:-^30}'.format('Saque Processado'))
print(f'{n50} notas de R$ 50\n{n20} notas de R$ 20\n{n10} notas de R$ 10\n{n1} notas de R$  1')