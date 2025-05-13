placa_veiculo = input("Digite a placa do carro ")
horas_estacionadas = int(input("Digite as horas que ficou estacionado "))

if horas_estacionadas < 2:
    print("O valor é R$ 5,00")

elif horas_estacionadas > 2:
    print("O valor é R$ 10,00")