valor_total = int(input("Digite o valor total da compra "))

if valor_total > 100:
    valor_final = valor_total * 5 / 100
    valor_total = valor_total - valor_final

print("o valor total da compra é de ", valor_total)