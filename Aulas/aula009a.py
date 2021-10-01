# Strings podem ser fatiadas em Python
frase = 'Curso em Video Python'
print(frase[9])

# Lembre-se, a indexação começa em 0, ou seja, "print(frase[0])" terá "C" como resultado.
print(frase[0])

# Em um fatiamento de uma faixa de caracteres, use ":" para separar o primeiro do último indice.
print(frase[3:9])

# Um terceiro item entre os colchetes "[9:20:2]" faz a seleção saltar de 2 em 2 caracteres.
print(frase[9:20:2])

# Omitir o primeiro ou último caractere no fatiamento fará a seleção ir até o primeiro ou último caractere.
print(frase[:5])

# O último item em uma fatia é sempre exclusive, ou seja, ele não aparece no resultado.
print(frase[0:1])

# Análise
len(frase)  # Mostra o tamanho do objeto analisado

frase.count('o', 0, 13)  # Conta quantas vezes o elemento aparece na variável. os números (opcionais) criam uma fatia
# onde o elemento deve ser procurado.

frase.find('deo')  # Informa em qual posição do indice o resultado aparece, se não houver resultado, ele retorna "-1"

print('Curso' in frase)  # Pesquisa o argumento e retorna um boolean

frase.replace('Python', 'Android')  # Substitui o primeiro argumento pelo segundo

frase.upper()  # Deixa tudo em maiúsculas. "lower()", "capitalize()", "title()" também efetuam alteração de caixa.
# capitalize(): deixa apenas a primeira letra da string em maiúscula
# title(): deixa a primeira letra de cada palavra em maiúscula

# Transformação
frase2 = '   Aprenda Python  '

frase2.strip()  # Remove os espaços em branco no inicio e fim da string. rstrip() e lstrip() pra retirar os espaços
# só de r = right ou l = left.

# Divisão
frase2.split()  # Separa a string em cada espaço, fazendo uma lista com a string
print(frase2[1][3])

# Junção
'-'.join(frase)  # Junta o string de volta, usando o argumento, no caso "-" como junção
print(frase2)

# Aspas triplas permitem que o comando tenha mais de uma linha
print('''Curso
em
Vídeo
Python''')
