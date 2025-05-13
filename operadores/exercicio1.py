import math
import os 


os.system('cls')
ponto_x1 = int(input("Digite o primeiro ponto "))
ponto_y1 = int(input("Digite o segundo ponto "))
ponto_x2 = int(input("Digite o terceiro ponto "))
ponto_y2 = int(input("Digite o quarto ponto "))

d = math.sqrt(((ponto_x1 - ponto_x2)** 2) + ((ponto_y1 - ponto_y2)** 2))

print("A distância entre os pontos é de ", d)