# Faça um programa que calcule a soma entre todos os números ímpares múltiplos de 3 entre 1 e 500.
soma = 0
for c in range(3, 500, 2):
    if c % 3 == 0:
        soma += c
print(soma)