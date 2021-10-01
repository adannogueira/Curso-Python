# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.
cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'magenta': '\033[35m',
         'ciano': '\033[36m',
         'branco': '\033[37m'}

value = input(f'{cores["azul"]}Digite algo: ')
print('{}A classe digitada é: {}.'.format(cores['vermelho'], type(value)))
print(f'{cores["amarelo"]}É alfabético: {value.isalpha()}')
print(f'{cores["verde"]}É alfanumérico: {value.isalnum()}')
print(f'{cores["ciano"]}É numérico: {value.isnumeric()}')
print(f'{cores["magenta"]}Está em maiúsculas: {value.isupper()}')
print(f'{cores["vermelho"]}Está em minúsculas: {value.islower()}')
print(f'{cores["branco"]}Está em ASCII: {value.isascii()}')
print(f'{cores["azul"]}É um espaço: {value.isspace()}')
print(f'{cores["amarelo"]}É imprimível: {value.isprintable()}')
print(f'{cores["verde"]}Está capitalizado: {value.istitle()}')
