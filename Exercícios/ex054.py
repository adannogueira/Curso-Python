# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
# Considere maioridade 21 anos
from datetime import date
nascimento = []
maiores = 0
menores = 0

for c in range(0, 7):
    nascimento.append(int(input(f'Digite o ano de nascimento da pessoa {c + 1}: ')))

for c in range(0, 7):
    if date.today().year - nascimento[c] >= 21:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} pessoas são maiores.\n{menores} pessoas são menores.')