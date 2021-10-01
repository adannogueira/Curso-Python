# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
# Importante: use cores.
from time import sleep


def pyhelp():
    while 1:
        print('\033[2;34;40m~\033[m' * 40)
        print(F'\033[2;34;40m{"SISTEMA DE AJUDA PyHELP":^40}\033[m')
        print('\033[2;34;40m~\033[m' * 40)
        sleep(2)
        biblioteca = input("Função ou Biblioteca > ").upper()
        if biblioteca == 'FIM':
            break
        sleep(1)
        print('\033[2;34;40m~\033[m' * 40)
        print(f'\033[2;34;40m{"ACESSANDO AJUDA PARA FUNÇÃO " + biblioteca:^40}\033[m')
        print('\033[2;34;40m~\033[m' * 40)
        sleep(2)
        print('\033[1;34;40m')
        help(biblioteca.lower())
        print('\033[m')
        sleep(4)


if __name__ == '__main__':
    pyhelp()
