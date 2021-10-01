# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1,00 = R$3,27

print('Olá, sou seu cambista virtual, me diga quantos reais você tem na carteira e te direi quantos dólares pode'
      ' comprar.')
rs = float(input('Digite o valor em carteira: \033[33mR$'))
dl = rs/3.27

print(f'\033[mCom seus R${rs:.2f}, você compra US${dl:.2f}! Desde que você não esteja em 2020...')
