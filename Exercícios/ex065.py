# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores  e qual foi o maior e menor valores digitados. O programa deve perguntar ao usuário se ele quer
# ou não continuar a digitar valores.

values = []

while True:
    value = int(input("Digite um número: "))
    cont = input("Deseja digitar mais números? [Y/N]: ").strip().upper()
    values.append(value)
    if cont[0] == 'N':
        break
soma = 0
for num in values:
    soma += num
values.sort()
soma = soma / len(values)
print(f'A média entre os números digitados é {soma}')
print(f'O maior número digitado foi {values[-1]} e o menor foi {values[0]}.')