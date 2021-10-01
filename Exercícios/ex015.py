# Escreva um programa que pergunte a quantidade de km percorridos por um caro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o caro custa R$60 por dia e R$0,15 por km rodado.
dias = int(input('Por quantos dias o cliete alugou o carro? '))
km = float(input('Quantos km foram percorrido nesse período? '))
diarias = dias * 60
rodagem = round(km) * 0.15
valor = diarias + rodagem
print(f'O valor a pagar considera:\nR${diarias:.2f} por {dias} diárias.\nR${rodagem:.2f} por {km}Km.')
print(f'O valor final a pagar é R${valor:.2f}.')
