# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

frase = str(input('Digite uma expressão contendo parênteses: '))
abre = list()
fecha = list()
for i, l in enumerate(frase):
    if l == '(':
        abre.append(i)
    if l == ')':
        fecha.append(i)
if len(abre) == 0 and len(fecha) > 0:
    print('Você esqueceu de abrir parêntese.')
if len(fecha) == 0 and len(abre) > 0:
    print('Você esqueceu de fechar parêntese.')
if len(abre) > 0 and len(fecha) > 0:
    if fecha[0] < abre[0]:
        print('Abra o parêntese antes de fechá-lo.')
    elif len(abre) > len(fecha):
        print('Você esqueceu de fechar algum parêntese.')
    elif len(abre) < len(fecha):
        print('Você esqueceu de abrir algum parêntese.')
    else:
        print('Tudo certo.')
if len(abre) == len(fecha) == 0:
    print('Sua expressão não contém parênteses.')
