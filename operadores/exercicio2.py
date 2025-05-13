import math
import os 

n = int(input("Digite o número de lados "))
s = int(input("Digite o comprimento de cada lado "))
a = (n * s **2) / (4 * math.tan(math.pi/n))

print('Essa é a área do polígono', a)