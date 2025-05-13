nome_produto = input("Digite o nome do produto: ")
valor_compra = int(input("Qual o valor da compra? "))

if valor_compra < 10:
    valor_total = valor_compra * 1.70
    print(valor_total)
elif valor_compra >= 10 and valor_compra < 30:
    valor_total = valor_compra * 1.50
    print(valor_total)
elif valor_compra >= 30 and valor_compra > 50:
    valor_total = valor_compra * 1.40
    print(valor_compra)
elif valor_compra >= 50:
    valor_total = valor_compra * 1.30
    print(valor_total)