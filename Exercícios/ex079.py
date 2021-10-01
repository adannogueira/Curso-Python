# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

def numerador():
    lista = []
    while True:
        try:
            c = int(input('Quantos números você irá digitar: '))
        except ValueError:
            print('Caractere inválido, só números inteiros são aceitos.')
            continue
        break
    while c > 0:
        try:
            n = int(input('Digite um número: '))
            if n not in lista:
                lista.append(n)
            c -= 1
        except ValueError:
            print('Caractere inválido, só números inteiros são aceitos.')
            continue
    return lista


if __name__ == '__main__':
    numeros = numerador()
    numeros.sort()
    print('Os números únicos em ordem crescente são: ', end='')
    for num in numeros: print(num, end=', ')
    print('Fim \n')
