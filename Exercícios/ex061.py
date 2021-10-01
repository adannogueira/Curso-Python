# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os dez primeiros termos da progressão
# usando a estrutura while

n = int(input("Início da PA: "))
r = int(input("Razão da PA: "))
c = 0
while c < 10:
    print(n, end=', ')
    n = n + r
    c += 1
print("Fim.")