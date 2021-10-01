# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
lista = [n1, n2, n3]

lista.sort()

if n1 == n2 and n1 == n3:
    print("Você escolheu três números iguais.")
else:
    print(f"O maior número é {lista[-1]}, o menor é {lista[0]}.")
