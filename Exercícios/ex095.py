# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

def cadastro_jogador():
    return {'Nome': str(input('Nome: ')), 'Partidas Jogadas': int(input("Partidas jogadas: "))}


def aproveitamento(jogador, partidas):
    total = 0
    for c in range(partidas):
        gols = int(input(f'Gols no jogo {c + 1}: '))
        jogador[f'Gols no Jogo {c + 1}'] = gols
        total += gols
    jogador['Total de Gols'] = total
    return jogador


if __name__ == '__main__':
    jogadores = []
    while 1:
        jogador = cadastro_jogador()
        jogador = aproveitamento(jogador, jogador.get('Partidas Jogadas'))
        jogadores.append(jogador)
        if str(input('Incluir outro [S/N]? '))[0].upper() == 'N':
            break

    print(f'Nº\tJOGADOR\t\tPARTIDAS')
    for i in range(len(jogadores)):
        count = 0
        for k, v in jogadores[i].items():
            print(f'{i + 1}\t{v}\t\t{jogadores[i].get("Partidas Jogadas")}')
            count += 1
            if count == 1:
                break

    while 1:
        aproveita = (int(input('Deseja detalhar o aproveitamento de qual jogador [999 para sair]: ')) - 1)
        if aproveita == 998:
            print('FIM')
            break
        elif aproveita < 0 or aproveita > (len(jogadores) - 1):
            print('Digite um número válido.')
        else:
            for k, v in jogadores[aproveita].items():
                print(f'{k}: {v}')
