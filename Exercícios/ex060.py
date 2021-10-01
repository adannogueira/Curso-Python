# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um número: '))
f = n - 1
while f > 0:
    n = n * f
    f -= 1
print(f'Fatorial: {n}')
