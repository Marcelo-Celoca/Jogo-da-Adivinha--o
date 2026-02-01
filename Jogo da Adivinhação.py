import random

cont = 0
num_secreto = random.randint(1, 10)
nome = input('Olá! Qual o seu nome? ')

while True:
    entrada = input(f'Digite seu palpite, \033[35m{nome}\033[m (números de 1 a 10): ')
    try:
        num_user = int(entrada)
    except ValueError:
        print('\033[31mOps! Esse não é um número válido! Tente novamente usando apenas algarismos.\033[m')
        continue

    cont += 1
    
    if num_user == num_secreto:
        print(f'\033[34mParabéns!\033[m Você acertou o número com {cont} tentativas.')
        break
    elif num_user < num_secreto:
        print('Mais alto!')
    else:
        print('Mais baixo!')
        
        



