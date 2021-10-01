# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa
# O programa deverá realizar a operação selecionada em cada caso.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
choice = 0
while not choice == 5:
    print('Menu\n---&---&---&---\n[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa')
    choice = int(input('Digite o número da opção: '))
    if choice == 1:
        print(f'\n{n1} + {n2} = {n1 + n2}')
    elif choice == 2:
        print(f'\n{n1} x {n2} = {n1 * n2}')
    elif choice == 3:
        if n1 > n2:
            print(f'\n{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'\n{n2} é maior que {n1}')
        else:
            print(f'\nAmbos os números são {n1}, não tem um maior...')
    elif choice == 4:
        n1 = int(input('\nDigite um número: '))
        n2 = int(input('Digite outro número: '))
print('---&---&---&---\nFIM DO PROGRAMA')