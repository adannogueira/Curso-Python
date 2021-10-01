# Escreva um programa que converta uma temperatura digitada em °C para ºF.
c = float(input('Digite a temperatura em graus Celsius: '))
f = c * 1.8 + 32
print(f'{c:.1f}°C correspondem a {f:.1f}°F.')
