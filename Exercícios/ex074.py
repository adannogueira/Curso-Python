# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
lista = [randint(0,100) for i in range(6)]
tupla = tuple(lista)
print(f'Os números aleatórios gerados foram {tupla}.')
var1 = sorted(tupla)[0]
var2 = sorted(tupla, reverse=True)[0]
print(f'O menor deles é {var1} e o maior é {var2}.')