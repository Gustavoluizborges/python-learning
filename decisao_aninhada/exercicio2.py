import math
a = float(input("Digite um número "))
b = float(input("Digite um número "))
c = float(input("Digite um número "))

delta = b ** 2 - 4 * a * c

if delta <= 0: 
    print("Não há raízes reais")
elif a == 0:
    print("Não é equação do segundo grau")
elif delta > 0:
    x1 = -b + math.sqrt(delta) / (2 * a)
    x2 = -b - math.sqrt(delta) / (2 * a)
 
print(x1, x2)