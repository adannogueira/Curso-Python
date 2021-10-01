# Estruturas condicionais
nome = str(input('Qual é o seu nome? '))
if nome == 'Adan':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal...')
print(f'Bom dia, {nome}.')

# Estrutura simplificada
nome = str(input('Qual o seu nome? '))
print('Que nome lindo!' if nome == "Adan" else 'Seu nome é tão normal...')
