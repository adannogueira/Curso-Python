# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
# um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

def leitor_alunos():
    return [input('Digite o nome do aluno: '), float(input('Nota 1: ')), float(input('Nota 2: '))]


def mediador(lista):
    return (lista[1] + lista[2]) / 2


def localizador(lista, num):
    return lista[num][1:]


if __name__ == '__main__':
    alunos = []
    while 1:
        alunos.append(leitor_alunos())
        if input('Deseja continuar [S/N]: ')[0] in 'Nn':
            break

    print(f'{"Nº":^3}{"Nome":^15}{"Média":^4}')
    for i, aluno in enumerate(alunos):
        print(f'{i:^3}{aluno[0]:^15}{mediador(aluno)}')

    while 1:
        opcao = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
        if opcao == 999:
            break
        print(localizador(alunos, opcao))
