# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
c = str(input('Digite o nome da cidade: ')).strip().lower()
s = c.find('santo')
if s == 0:
    print('O nome da cidade começa com Santo.')
else:
    print('O nome da cidade não começa com Santo.')

# Método que usa boolean como resposta
print(c[0:5] == "santo")
