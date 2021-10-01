# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são suas vogais.

tupla = ('abelha', 'cachorro', 'bicicleta', 'calça', 'atum', 'biscoito', 'pedra', 'elefante')

for word in tupla:
    print(word, end=' >> ')
    for letter in word:
        if letter in 'aeiou':
            print(letter, end=' ')
    print('\n')