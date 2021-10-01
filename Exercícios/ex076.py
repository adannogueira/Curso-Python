# Crie um programa que tenha uma tupla única com nomes de produtos e seu respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

precos = ('Coca Cola', 2.50, 'Pastel', 3, 'Coxinha', 2.7, 'Fanta', 2.3, 'Pepsi', 1.99, 'Misto', 3, 'X-Tudão', 10.5)
print('{:=^35}'.format('LISTA DE PREÇOS'))
for c in range(0, len(precos), 2):
    print(f"{precos[c]:.<29}{precos[c + 1]:.>6.2f}")
