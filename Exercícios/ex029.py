# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
v = float(input("Digite a velocidade do veículo registrada no radar: "))
if v <= 80:
    print("Boa viagem, dirija com cuidado.")
else:
    m = (v - 80) * 7
    print(f"Você está indo rápido demais, o valor da multa é de R$ {m:.2f}.")
