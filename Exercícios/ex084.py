# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

def cadastro_de_pacientes():
    pacientes = []
    while 1:
        pacientes.append(str(input('Digite o nome: ')))
        pacientes.append(float(input('Digite o peso: ')))
        saida = input('Continuar? (S/N) ')[0].upper()
        if saida in 'N':
            break
    return pacientes


def contar_cadastrados(lista):
    return len(lista) // 2


def mais_pesados(lista):
    maior_peso = lista[1]
    for c in range(1, len(lista), 2):
        if lista[c] > maior_peso:
            maior_peso = lista[c]
    return maior_peso


def mais_leves(lista):
    menor_peso = lista[1]
    for c in range(1, len(lista), 2):
        if lista[c] < menor_peso:
            menor_peso = lista[c]
    return menor_peso


def nomes_pesados(lista, peso):
    return [lista[c - 1] for c in range(len(lista)) if lista[c] == peso]


def nomes_leves(lista, peso):
    return [lista[c - 1] for c in range(len(lista)) if lista[c] == peso]

if __name__ == '__main__':
    lista_de_pacientes = cadastro_de_pacientes()
    total_de_cadastros = contar_cadastrados(lista_de_pacientes)
    print(f'Ao todo foram cadastradas {total_de_cadastros} pessoas.\n')
    if total_de_cadastros <2:
        print(f'Você só cadastrou uma pessoa, {lista_de_pacientes[0]}, que pesa {lista_de_pacientes[1]}kg.')
    else:
        print(f'O maior peso registrado é {mais_pesados(lista_de_pacientes)}, registrado por: ', end='')
        for name in nomes_pesados(lista_de_pacientes, mais_pesados(lista_de_pacientes)):
            print(f'{name}',end=', ')
        print('\n')
        print(f'O menor peso registrado é {mais_leves(lista_de_pacientes)}, registrado por: ', end='')
        for name in nomes_leves(lista_de_pacientes, mais_leves(lista_de_pacientes)):
            print(f'{name}', end=', ')
        print('\n')
