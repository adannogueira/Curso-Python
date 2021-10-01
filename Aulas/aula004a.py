# Operações básicas

# Delimitador ' ' ou " ", sendo aspas simples o padrão
# Mensagens obrigatóriamente precisam de aspas para serem corretamente interpretadas
# A funções tem parênteses. Ex: print()

print('Olá, mundo!')

# Números não precisam das aspas delimitadoras
# Diferente dos textos, números são típicamente usaddos para cálculos

print(7+4)

# Para usar os números como mensagens, use aspas, observe que no exemplo abaixo não há a operação de adição
# Apenas a concatenação das mensagens, agora tratadas como strings devido as aspas

print('7'+'4')

# Para separar informações dentro da função, use virgula ,

print('Olá', 5)

# Informações são armazenadas em variáveis, em Python, toda variável é um objeto.
# Dê preferência para letras minúsculas

nome = 'Adan'
idade = 34
peso = '80kg'

print(nome, idade, peso)

# A função input() recebe como valor o que é digitado pelo usuário

nome = input('Qual é seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Qual é o seu peso? ')

print(nome, idade, peso)
