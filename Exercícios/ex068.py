# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
wins = 0
print('--&-' * 10, '\nVamos jogar PAR ou Ímpar!')
while 1:
    print('-&--' * 10)
    n1 = int(input("Qual número você escolhe? "))
    n2 = randint(0,10)
    opcao = str(input('\nPar ou ímpar? [P/I]: ')).strip().upper()[0]
    while opcao not in 'PI':
        opcao = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    soma = n1 + n2
    sleep(1)
    if opcao == 'P':
        print('PAR!', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('ÍMPAR!')
        sleep(2)
    else:
        print('ÍMPAR!', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('PAR!')
        sleep(2)

    if soma % 2 == 0:
        if opcao == 'P':
            print('-&--' * 10)
            print(f'Você escolheu {n1}, eu escolhi {n2}, o total é {soma}, que é PAR, você ganhou!')
            print('Vamos jogar outra vez')
            wins += 1
        else:
            print('-&--' * 10)
            print(f'Você escolheu {n1}, eu escolhi {n2}, o total é {soma}, que é PAR, você perdeu!')
            print('Fim de jogo.')
            break
    else:
        if opcao == 'I':
            print('-&--' * 10)
            print(f'Você escolheu {n1}, eu escolhi {n2}, o total é {soma}, que é ÍMPAR, você ganhou!')
            print('Vamos jogar outra vez')
            wins += 1
        else:
            print('-&--' * 10)
            print(f'Você escolheu {n1}, eu escolhi {n2}, o total é {soma}, que é ÍMPAR, você perdeu!')
            print('Fim de jogo.')
            break
print(f'Você fez {wins} pontos ao todo!')