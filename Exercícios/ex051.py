# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
n = int(input("Início da PA: "))
r = int(input("Razão da PA: "))
for c in range(n, (r * 10) + n, r):
    print(c, end=', ')
print("Fim.")