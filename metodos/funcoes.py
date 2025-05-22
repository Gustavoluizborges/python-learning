import os
import time

def areaQuadrado (lado, altura):
    return lado * altura

def areaTriangulo (base, altura):
    return (base * altura) / 2

def areaTrapezio (baseMaior, baseMenor, altura):
    return ((baseMaior + baseMenor) * altura) / 2

def limpar():
    time.sleep(4)
    os.system('cls')
