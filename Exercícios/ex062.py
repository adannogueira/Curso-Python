# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

n = int(input("Início da PA: "))
r = int(input("Razão da PA: "))
c = 0
while 1:
    while c < 10:
        print(n, end=', ')
        n = n + r
        c += 1
    print('\n')
    term = int(input("Deseja mostrar mais termos? Quantos?: "))
    if term == 0:
        break
    else:
        c = c - term
print("Fim.")