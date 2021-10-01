# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep


def rolador_de_dados():
    return {
        'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)
    }


if __name__ == '__main__':
    jogos = rolador_de_dados()
    print('Rolando os dados:')
    sleep(1)

    for k, v in jogos.items():
        print(f'{k} rolou um {v}!')
        sleep(1)
    print('-=#=' * 6)
    sleep(1)
    print('Anunciando colocações:')
    sleep(1)

    for c in range(6, 0, -1):
        for k, v in jogos.items():
            if v == c:
                print(f'{k} fez {v} pontos.')
                sleep(1)
    print('FIM DE JOGO')
