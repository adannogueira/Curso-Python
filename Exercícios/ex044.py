# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagto.
# À Vista dinheiro/cheque 10% de desconto
# À vista no cartão 5% de desconto
# Em até 2 x cartão preço normal
# 3x ou mais no cartão 20% de juros
preco = float(input("Digite o valor do produto: R$ "))
condicao = int(input("Forma de pagamento:\n1 - À Vista Dinheiro\n2 - À Vista Cartão\n3 - 2 x Cartão\n4 - À Prazo\n"))
if condicao == 1:
    print(f"Para pagamento à vista em dinheiro/cheque, com 10% de desconto: R$ {preco * 0.9:.2f}.")
elif condicao == 2:
    print(f"Para pagamento à vista no cartão, com 5% de desconto: R$ {preco * 0.95:.2f}.")
elif condicao == 3:
    print(f"Para pagamento em até 2 parcelas no cartão, preço normal: R$ {preco:.2f}.")
elif condicao == 4:
    parc = int(input("Quantas parcelas: "))
    print(f"""Para pagamento em {parc} parcelas no cartão, juros de 20%: R$ {preco * 1.2:.2f}.
    {parc} x R$ {(preco * 1.2) / parc:.2f}""")
else:
    print("Escolha uma forma de pagamento válida.")
