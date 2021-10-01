# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um: ')),
         int(input('Agora o último: ')))
a = tupla.count(9)
print(f'O número 9 aparece {a} vezes.')

b = tupla.index(3)
print(f'O número 3 aparece na {b + 1}ª posição.')

print(f'Os número pares são: ', end='')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')
print('\nFim!')