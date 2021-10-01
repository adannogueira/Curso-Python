# Crie um programa que faça o computado jogar Jokempô com você.
import random
import time

# Título do jogo
print("\033[34m=#-" * 6)
print("#     JOKEMPÔ    =")
print("-=#" * 6)

# Variáveis
jokempo = ['pedra', 'papel', 'tesoura']
pc_pontos = 0
pl_pontos = 0


# Função para avaliar quem vence
def game(pc, pl):
    if pc == pl:
        return 0
    elif pc == 'pedra':
        if pl == 'tesoura':
            return 1
        else:
            return 2
    elif pc == 'tesoura':
        if pl == 'papel':
            return 1
        else:
            return 2
    elif pc == 'papel':
        if pl == 'pedra':
            return 1
        else:
            return 2


# Loop de jogo, melhor de 3
while True:
    if pc_pontos == 2 or pl_pontos == 2:
        break
    print(f"=-=-=-=-=-=-=-=-=-\nJogador {pl_pontos} x {pc_pontos} Computador")
    pc_escolhe = random.choice(jokempo)
    time.sleep(1)
    pl_escolhe = str(input("Pedra, papel ou tesoura? ")).strip().lower()
    if pl_escolhe not in "pedra papel tesoura":
        print("Escolha uma das três opções válidas.")
        time.sleep(2)
        continue
    else:
        ponto = game(pc_escolhe, pl_escolhe)
        if ponto == 0:
            time.sleep(1)
            print(f"Jogador: {pl_escolhe}\nComputador: {pc_escolhe}")
            time.sleep(2)
            print("Empate!")
            continue
        elif ponto == 1:
            time.sleep(1)
            print(f"Jogador: {pl_escolhe}\nComputador: {pc_escolhe}")
            pc_pontos += 1
            time.sleep(2)
            print("Ponto para o computador!")
            continue
        elif ponto == 2:
            time.sleep(1)
            print(f"Jogador: {pl_escolhe}\nComputador: {pc_escolhe}")
            pl_pontos += 1
            time.sleep(2)
            print("Ponto para o jogador!")
            continue
print(f"Placar Final\nJogador {pl_pontos} x {pc_pontos} Computador")
if pl_pontos >= 2:
    print("Fim de jogo, você venceu!")
else:
    print("Fim de jogo, você perdeu.")
