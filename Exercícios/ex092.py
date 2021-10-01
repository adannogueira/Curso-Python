# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date


def idade(ano):
    return date.today().year - ano


def cad_pessoa():
    return {'Nome': str(input('Nome: ')), 'Idade': idade(int(input('Ano de Nascimento: ')))}


def cad_trabalhador(person, mtps):
    trabalhador = person
    trabalhador['CTPS'] = mtps
    trabalhador['Contratação'] = int(input('Ano de Contratação: '))
    trabalhador['Salário'] = float(input('Salário: '))
    trabalhador['Idade de Aposentadoria'] = aposentadoria(trabalhador.get('Contratação'), trabalhador.get('Idade'))
    return trabalhador


def aposentadoria(inicio, nasc):
    return ((inicio + 35) - date.today().year) + nasc


if __name__ == '__main__':
    pessoa = cad_pessoa()
    ctps = int(input('Nº da CTPS [0 - Não tem]: '))
    if ctps != 0:
        pessoa = cad_trabalhador(pessoa, ctps)
    print('CADASTRO EFETUADO')
    for k, v in pessoa.items():
        print(f'{k}: {v}')
