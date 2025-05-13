fatura = 0
numero_digitado = 0
fatura_proxima = 0

while numero_digitado != 4:
    print("\nCartão de Crédito!")
    print("Próxima fatura: R$", f"{fatura:.2f}")

    numero_digitado = int(
        input(
            "\n[1] Adicionar compra\n[2] Pagar fatura\n[3] Ver próxima fatura\n[4] Sair\nEscolha uma opção: "
        )
    )

    if numero_digitado == 1:
        valor_compra = float(input("Digite o valor da compra: "))
        if valor_compra > 0:
            fatura += valor_compra
        else:
            print("Valor inválido!")

    elif numero_digitado == 2:
        valor_pagar = input(
            "Deseja pagar o valor total ou apenas o valor mínimo? (Total/Valor mínimo): "
        )

        if valor_pagar.lower() == "valor mínimo":
            desconto = fatura * 0.10
            fatura_proxima = fatura - desconto
            fatura = 0
            print("Você pagou o valor mínimo.")
        elif valor_pagar.lower() == "total":
            fatura = 0
            fatura_proxima = 0
            print("Fatura paga totalmente.")
        else:
            print("Opção inválida!")

    elif numero_digitado == 3:
        print("Sua próxima fatura é: R$", f"{fatura_proxima:.2f}")

    elif numero_digitado == 4:
        print("Programa encerrado!")
    else:
        print("Opção inválida. Tente novamente.")
