# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

array = []
for d in range(5):
    n = int(input('Digite um número: '))
    if len(array) < 1:
        array.append(n)
    else:
        if array[-1] < n:
            array.append(n)
        else:
            for c, i in enumerate(array):
                if n < i:
                    array.insert(c, n)
                    break

print('Os números digitados, em ordem crescente são: ', end='')
for n in array:
    print(f'{n}', end=', ')
print('FIM.')
