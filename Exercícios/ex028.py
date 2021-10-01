# Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

i = randint(0, 5)
print("--&-" * 18)
a = int(input("Eu estou pensando em um número entre 1 e 5, consegue adivinhar qual é? "))
print("Processando...")
sleep(3)
if a == i:
    print(f"Isso mesmo, eu pensei em {i}, parabéns, você acertou!")
elif a > 5 or a < 0:
    print(f"Eu estava pensando em {i}, entre 0 e 5, lembra? Você nem chegou perto.")
else:
    print(f"Você disse {a}, eu pensei em {i}, não foi dessa vez.")
print("FIM DO JOGO")
print("--&-" * 18)