# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

def digita_valores():
    lista = [[], []]
    for c in range(7):
        temp = int(input(f'Digite o {c+1}º número: '))
        if temp % 2 == 0:
            lista[0].append(temp)
        else:
            lista[1].append(temp)
    return sorted(lista)


if __name__ == '__main__':
    valores = digita_valores()
    print(f'Os valores pares digitados são: {valores[0]}')
    print(f'Os valores ímpares digitados são: {valores[1]}')
