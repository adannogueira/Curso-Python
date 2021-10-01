# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Exemplo: Número: 1834.
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
i = int(input('Digite um número inteiro de 0 a 9999: '))

# A fórmula abaixo separa os números individualmente, independente da quantidade de números
u = i // 1 % 10
d = i // 10 % 10
c = i // 100 % 10
m = i // 1000 % 10

# Para separação como string
if i >= 0 and i <= 9999:
    i = i + 10000
    i = str(i)
    print(f'Unidade: {i[4]}')
    print(f'Dezena:  {i[3]}')
    print(f'Centena: {i[2]}')
    print(f'Milhar:  {i[1]}')
else:
    print('Você não digitou um número válido.')
