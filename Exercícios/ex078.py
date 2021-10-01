# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.

numeros = [int(input('Digite um número: ')) for c in range(5)]

maior = max(numeros)
menor = min(numeros)

num_maior = []
num_menor = []

for c in range(len(numeros)):
    if numeros[c] == maior:
        num_maior.append(c)
    if numeros[c] == menor:
        num_menor.append(c)

print(f'O maior número digitado foi {maior} com índice ', end="")
for num in num_maior: print(num, end=" ")
print(f'\nO menor número digitado foi {menor} com índice ', end="")
for num in num_menor: print(num, end=" ")
print('\n')
