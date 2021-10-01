# Faça um programa que leia um ano qualquer e mostre se ele é bisexto.
from datetime import date

a = int(input("Digite o ano, use 0 para o ano atual: "))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f"O ano de {a} é bisexto.")
else:
    print(f"O ano de {a} não é bisexto.")
