# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

n = str(input('Digite seu nome completo: ')).lower().strip()
s = n.count('silva')
if s >= 1:
    print('Seu nome contém Silva.')
else:
    print('Seu nome não contém Silva.')

# Método com boolean
print("silva" in n)
