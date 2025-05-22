import funcoes

while True:
    print ('O que deseja calcular?')
    escolha = int(input('[1] Área do Quadrado\n[2] Área do Triângulo\n[3] Área do Trapézio\n'))

    if escolha == 1:
        lado = int(input('Digite a medida do lado: '))
        altura = lado
        print(f'A área do quadrado é {funcoes.areaQuadrado(lado,altura)}')
        funcoes.limpar()
    
    elif escolha == 2:
        base = int(input('Digite a medida da base: '))
        altura = int(input('Digite a medida da altura: '))
        print(f'A área do triângulo é {funcoes.areaTriangulo(base,altura)}')
        funcoes.limpar()

    elif escolha == 3:
        baseMaior = int(input('Digite a medida da base maior: '))
        baseMenor = int(input('Digite a medida da base menor: '))
        altura = int(input('Digite a medida da altura: '))
        print(f'A área do trapézio é {funcoes.areaTrapezio(baseMaior,baseMenor,altura)}')
        funcoes.limpar()
    else:
        break
