# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, dessa vez use FOR.
num = int(input("Número para tabuada: "))
print("TABUADA")
for c in range(1, 11):
    print(f"{num} x {c:2d} = {num * c}")