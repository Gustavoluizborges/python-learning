valorPrestacao = int(input("Qual o valor da prestação? "))
multa = int(input("Qual a porcentagem de multa pelo atraso? "))
qtdeDias = int(input("E qual a quantidade de dias? "))
prestação = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

print("O valor da prestação é ", prestação)