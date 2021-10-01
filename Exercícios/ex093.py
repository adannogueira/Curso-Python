# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

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

    for i in range(len(jogadores)):
        print(f'JOGADOR {i + 1}\tPARTIDAS')
        count = 0
        for k, v in jogadores[i].items():
            print(f'{k}: {v}')
            count += 1
            if count == 2:
                break


