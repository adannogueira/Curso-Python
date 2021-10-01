# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Exemplo: 6.12 >> "O número 6.12 tem a parte inteira 6".
from math import trunc
num = float(input('Digite um número real qualquer: '))
print(f'A parte inteira de {num} é {trunc(num)}.')
