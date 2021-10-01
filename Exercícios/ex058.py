# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários.

from random import randint
from time import sleep

i = randint(0, 10)
print("--&-" * 19)
a = int(input("Eu estou pensando em um número entre 0 e 10, consegue adivinhar qual é? "))
tries = 1

while i != a:
    print("Processando...")
    sleep(2)
    a = int(input(f"Você disse {a}, mas não é esse, tente outra vez: "))
    tries += 1
print("Processando...")
sleep(2)
print(f"Isso mesmo, eu pensei em {i}, parabéns, você acertou!\nVocê deu {tries - 1} palpites errados.")
print("FIM DO JOGO")
print("--&-" * 19)