# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas dos que forem pares.
# Se for ímpar, desconsidere.
soma = 0
for c in range(1, 7):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n
print(f"A soma dos pares é: {soma}")