# Crie um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez
f = str(input('Digite uma frase qualquer: ')).lower().strip()
print(f'A letra "a" aparece {f.count("a")} vezes.')
if f.count("a") > 0:
    print(f'Ela aparece pela primeira vez na posição {f.find("a") + 1}.')
    print(f'E pela última vez na posição {f.rfind("a") + 1}.')
else:
    print('Não há contagem a ser feita.')
