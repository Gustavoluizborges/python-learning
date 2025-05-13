consumo_kwh = float(input("Digite seu consumo de energia em kWh "))

if consumo_kwh <= 100:
    print(consumo_kwh * 0.50)
elif consumo_kwh <= 300:
    print(consumo_kwh * 0.75)
else: 
 print(consumo_kwh * 1.0)