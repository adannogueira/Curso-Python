# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário, 2 para octal e 3 para hexadecimal
num = int(input("Digite um número inteiro qualquer: "))
base = int(input("""Escolha a base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
Opção: """))

if base < 1 or base > 3:
    print("As opções válidas são: 1, 2 e 3.")
elif base == 1:
    binario = bin(num)
    print(f"O valor {num} equivale a {binario[2:]} em base binária.")
elif base == 2:
    octal = oct(num)
    print(f"O valor {num} equivale a {octal[2:]} em base octal.")
else:
    hexa = hex(num)
    print(f"O valor {num} equivale a {hexa[2:]} em base hexadecimal.")
