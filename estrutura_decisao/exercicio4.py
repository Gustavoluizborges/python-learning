valor_agua = int(input("Digite o valor da conta de água "))
valor_telelfone = int(input("Digite o valor da conta de telelfone "))
valor_energia = int(input("Digite o valor da conta de energia "))
valor_salario = int(input("Digite o valor do seu salário "))
valor_total_contas = valor_energia + valor_telelfone + valor_agua

if valor_salario < valor_total_contas:
    print("Salário insuficiente!")
else:
    valor_final = valor_total_contas - valor_salario
    print(valor_final)