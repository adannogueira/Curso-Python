# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

def pessoa():
    return {'Nome': str(input('Nome: ')), 'Sexo': str(input('Sexo: '))[0].upper(), 'Idade': int(input('Idade: '))}


def conta_pessoas(x):
    return len(x)


def media_idade(lst, x):
    age = 0
    for i in range(x):
        age += lst[i].get('Idade')
    return age / x


def mulheres(lst, x):
    return [lst[i].get('Nome') for i in range(x) if lst[i].get('Sexo') == 'F']


def acima_da_media(lst, med, x):
    return [lst[i].get('Nome') for i in range(x) if lst[i].get('Idade') > med]


if __name__ == '__main__':
    quantidade = int(input('Quantas pessoas deseja cadastrar: '))
    pessoas = []
    for i in range(quantidade):
        pessoas.append(pessoa())
    print(f'Você cadastrou {quantidade} pessoa(s).')
    med_idade = media_idade(pessoas, quantidade)
    quant_mulheres = mulheres(pessoas, quantidade)
    acima = acima_da_media(pessoas, med_idade, quantidade)
    print(f'A média de idade é {med_idade:.0f}.')
    print('As mulheres cadastradas são:')
    for mulher in quant_mulheres:
        print(f'{mulher}')
    print('\nAs pessoas com idade acima da média são:')
    for velho in acima:
        print(f'{velho}')
