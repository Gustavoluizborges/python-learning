import math
import os 

valor_graus = float(input("Digite o valor em graus"))
conversor = math.radians(valor_graus)

seno = math.sin(conversor)
cosseno = math.cos(conversor)
tangente = math.tan(conversor)

print(f'Os valor de seno é {seno}, do cosseno {cosseno} e da tangente é de {tangente}')