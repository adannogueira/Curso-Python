# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999.
# Que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
# Desconsidere o 999
n = 0
digitados = 0
soma = 0
while 1:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        print('Condição de saída digitada, encerrando loop.')
        break
    else:
        digitados += 1
        soma += n
print(f'Você digitou {digitados} números, a soma de todos é {soma}.')