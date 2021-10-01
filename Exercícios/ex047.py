# Crie um programa que mostre na tela todos os números pares que estão no intervalo 1 a 50.
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print()
# Sem utilizar if
for par in range(2, 51, 2):
    print(par, end=' ')