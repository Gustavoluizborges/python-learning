import random
import time
import os

def espera_limpa():
    time.sleep(3)
    os.system('cls')

nome_usuario = input('Seja bem vindo! Qual seu nome? ')
print (f'Olá {nome_usuario}, te desafio a jogar comigo!')
espera_limpa()
print ('Escolha um número entre 0 e 10...')
espera_limpa()
print ('Se pensar o mesmo que o meu você ganha!!!')


while True:

        inicio = int(input(f'Vamos lá?\n[1] To pronto!\n[2] Sair\n'))

        if inicio == 1:
            numero_aleatorio = random.randint(0,10)
            print ('Boa sorte!!!')
            tentativa = int(input('Digite sua tentativa: '))
            
            if numero_aleatorio == tentativa:
                print('Caramba!!! Parece que você me derrotou...')
                break
            elif numero_aleatorio not in range(0, 11):
                 print('Esse número não está entre 0 e 10')
            else:
                print (f'Você errou... o número era {numero_aleatorio}')
                espera_limpa()

        elif inicio not in [1, 2]:
            print('Número inválido')
            espera_limpa()
        
        elif inicio == 2:
            print('Valeu! Até mais...')
            break
