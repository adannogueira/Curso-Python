# Faça um programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor.
print("Digite abaixo o peso das pessoas em kg.")
pesos = list()
for c in range(0, 5):
    pesos.append(float(input(f"Pessoa {c + 1}: ")))

pesos.sort()
print(f"O menor peso é {pesos[0]}kg.")
print(f"O maior peso é {pesos[4]}kg.")
