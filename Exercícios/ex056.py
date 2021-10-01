# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final mostre:
# Média de idade do grupo
# Nome do homem mais velho
# Quantas mulheres tem menos de 20 anos
from statistics import mean
nomes = list()
idades = list()
sexos = list()
age = 0
ppl = 0
wom = 0

for n in range(0, 4):
    print(f"Pessoa {n + 1}")
    nomes.append(input("Nome: "))
    idades.append(int(input("Idade: ")))
    sexos.append(input("Sexo (M/F): ").upper().strip())

print(f"A média de idade é {mean(idades)} anos.")

for c in range(0, 4):
    if idades[c] > age and sexos[c] == "M":
        age = idades[c]
        ppl = c

print(f"O Homem mais velho é {nomes[ppl]}, com {age} anos.")

for c in range(0, 4):
    if sexos[c] == "F" and idades[c] < 20:
        wom += 1

print(f"{wom} mulheres tem menos de 20 anos.")
