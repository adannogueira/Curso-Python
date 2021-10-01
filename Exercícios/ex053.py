# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo.
# Desconsiderando os espaços.
frase = str(input("Frase: ")).strip().lower().split()
frase = ''.join(frase)
frase = frase.replace('.', '')
frase = frase.replace(',', '')
frase = frase.replace('?', '')
frase = frase.replace('!', '')
frase = list(frase)
inverso = frase[::-1]
if frase == inverso:
    print('Sua frase é um palíndromo.')
else:
    print('Sua frase não é um palíndromo.')
