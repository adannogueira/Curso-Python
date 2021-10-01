# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
total = 0
caros = 0
barato = ' '
produto = 0
print('+--------------+\n| LOJÃO DO JÃO |\n+--------------+')
while 1:
    nome = input('Nome do Produto: ')
    preco = float(input('Preço do Produto: R$ '))
    total += preco
    if barato == ' ':
        barato = preco
        produto = nome
    else:
        if preco < barato:
            barato = preco
            produto = nome
    if preco > 1000:
        caros += 1
    prod = ' '
    while prod not in 'SN':
        prod = input('Comprar mais produtos? [S/N] ').strip().upper()[0]
    if prod == 'N':
        break
print('+--------------+\n|  CONCLUÍDO!  |\n+--------------+')
print(f'O valor total é R$ {total:.2f}\n{caros} Produto(s) custa(m) mais de R$ 1000,00')
print(f'O produto mais barato foi {produto}, custando R$ {barato:.2f}.')

