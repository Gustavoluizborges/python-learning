sinal = input("Digite qual o sinal da operação ")
a = float(input("Digite um número "))
b = float(input("Digite outro número "))

if sinal == "+":
    resultado = a + b
    print(resultado)
elif sinal == "-":
    resultado = a - b
    print(resultado)
elif sinal == "/":
    resultado = a / b
    print(resultado)
elif sinal == "*":
    resultado = a * b
    print(resultado)