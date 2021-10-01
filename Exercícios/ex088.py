# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint

def palpiteiro(num):
    lista = []
    for n in range(num):
        lista.append([])
        counter = 0
        while 1:
            namber = randint(1, 60)
            if namber not in lista:
                lista[n].append(randint(1,60))
                counter += 1
            if counter == 6:
                break
    return lista


if __name__ == '__main__':
    numero = int(input('Quantos bilhetes da MEGA você quer gerar: '))
    palpites = palpiteiro(numero)
    print('Aqui estão seus resultados:')
    for palpite in palpites:
        print(palpite)