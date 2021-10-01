# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para mais longas
i = float(input("Qual a distancia do seu destino em km: "))
if i <= 200:
    print(f"O valor da passagem é R${i * 0.5:.2f}.")
else:
    print(f"O valor da passagem é R${i * 0.45:.2f}.")
