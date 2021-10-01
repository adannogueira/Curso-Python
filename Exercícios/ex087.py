# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

from ex086 import matrixer

def soma_pares(matriz):
    pares = 0
    for c in range(len(matriz)):
        for d in range(len(matriz[c])):
            if matriz[c][d] % 2 == 0:
                pares += matriz[c][d]
    return pares


def soma_coluna(matriz, coluna):
    soma = 0
    for c in range(len(matriz)):
        soma += matriz[c][coluna]
    return soma


def maior_valor(matriz, linha):
    valor = matriz[linha][0]
    for num in matriz[linha]:
        if num > valor:
            valor = num
    return valor


if __name__ == '__main__':
    matriz = matrixer()
    for n, i in enumerate(matriz):
        for o, j in enumerate(matriz[n]):
            print(f'[{matriz[n][o]:^5}]', end='')
        print('')
    
    print(f'Os valores pares digitados somados resultam em {soma_pares(matriz)}!')
    print(f'Os valores da terceira coluna somados totalizam {soma_coluna(matriz, 2)}.')
    print(f'O maior número constante na linha 2 é {maior_valor(matriz, 1)}')