valor_compra = int(input("Digite o valor da compra "))

if valor_compra > 200:
    novo_valor = valor_compra / 5
    valor_compra = valor_compra - novo_valor
    print(valor_compra)
else:
    print(valor_compra)