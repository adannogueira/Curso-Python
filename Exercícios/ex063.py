# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# sequência de Fibbonacci.
#Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

counter = int(input('Sequência Fibo de: '))
c = 0
n1 = 0
n2 = 1
while c < counter:
    c += 1
    print(n1, end=', ')
    temp = n1
    n1 += n2
    n2 = temp
print('FIM!')