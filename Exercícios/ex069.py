# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
a = b = c = 0
while True:
    print(f'--&-' * 5, '\n      CADASTRO      ')
    print('-&--' * 5)
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in "MF":
        sexo = input('Sexo [M/F]: ').strip().upper()[0]
    print('--&-' * 5)
    if idade >= 18:
        a += 1
    if sexo == 'M':
        b += 1
    if sexo == 'F' and idade < 20:
        c += 1
    cont = ' '
    while cont not in 'SN':
        cont = input('Adicionar outro? [S/N]: ').strip().upper()[0]
    if cont == 'N':
        break
print(f'Ao todo foram cadastrados:\n{a} maiores de 18 anos\n{b} homens\n{c} mulheres menores de 20 anos')
