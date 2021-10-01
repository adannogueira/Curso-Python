# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre
# a matriz na tela, com a formatação correta.

def matrixer():
    matriz = [[], [], []]
    for c in range(3):
        for d in range(3):
            matriz[c].append(int(input(f'Digite um valor para [{c}, {d}]: ')))
    return matriz

if __name__ == '__main__':
    matriz = matrixer()
    for n, i in enumerate(matriz):
        for o, j in enumerate(matriz[n]):
            print(f'[{matriz[n][o]:^5}]', end='')
        print('')