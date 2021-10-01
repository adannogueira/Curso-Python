# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

from urllib.request import urlopen

try:
    funciona = urlopen('http://pudim.com.br/', timeout=5)
    print('O site pudim.com.br está no ar!')
except:
    print('Site fora do ar.')
