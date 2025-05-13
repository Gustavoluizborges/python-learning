turno_trabalho = input("Digite seu turno de trabalho ")
horas_trabalhadas = int(input("Digite suas horas trabalhadas "))

if turno_trabalho == "N":
    horas_totais = horas_trabalhadas * 45
else:
    horas_totais = horas_trabalhadas * 37.50
 
print(horas_totais)