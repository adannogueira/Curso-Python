# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Digite um número inteiro: "))
primo = 0
for c in range(2, n):
    if n % c == 0:
        primo += 1
if primo == 0:
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")
