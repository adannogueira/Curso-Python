# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras em maiúsculas
# O nome com todas minúsculas
# Quantas letras no total (sem considerar espaços)
# Quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
espaco = nome.count(' ')
primeiro = len(nome.split()[0])
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nome) - espaco} letras.')
print(f'Seu primeiro nome tem {primeiro} letras.')
