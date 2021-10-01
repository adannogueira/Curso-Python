# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
i = int(input("Digite um número inteiro: "))
e = i % 2
if i == 0:
    print("Agora você me pegou, 0 é par ou ímpar?")
elif e == 0:
    print(f"{i} é par.")
else:
    print(f"{i} é ímpar.")
