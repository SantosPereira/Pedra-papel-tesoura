"""
TO DO: Emitir sons quando houver vitória ou derrota no jogo
"""
from random import randint as random
from time import sleep
import os

os.system('cls')

sleep(0.5)
print('''\n\n\n
▒█▀▀█ █▀▀ █▀▀▄ █▀▀█ █▀▀█ ░░ 　 ▒█▀▀█ █▀▀█ █▀▀█ █▀▀ █░░ 　 █▀▀█ █░░█ 　 ▀▀█▀▀ █▀▀ █▀▀ █▀▀█ █░░█ █▀▀█ █▀▀█ 
▒█▄▄█ █▀▀ █░░█ █▄▄▀ █▄▄█ ▄▄ 　 ▒█▄▄█ █▄▄█ █░░█ █▀▀ █░░ 　 █░░█ █░░█ 　 ░▒█░░ █▀▀ ▀▀█ █░░█ █░░█ █▄▄▀ █▄▄█ 
▒█░░░ ▀▀▀ ▀▀▀░ ▀░▀▀ ▀░░▀ ░█ 　 ▒█░░░ ▀░░▀ █▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀▀ ░▀▀▀ 　 ░▒█░░ ▀▀▀ ▀▀▀ ▀▀▀▀ ░▀▀▀ ▀░▀▀ ▀░░▀ 

▀█░█▀ ▄█░ ░ █▀▀█ 
░█▄█░ ░█░ ▄ █▄▀█ 
░░▀░░ ▄█▄ █ █▄▄█\n\n''')
sleep(1)




def play():
    print('Escolha:\n[\033[1;31m1\033[0;0m] Para Pedra\n[\033[1;31m2\033[0;0m] Para Papel\n[\033[1;31m3\033[0;0m] Para Tesoura\n\n\n\n')
    sleep(1)
    '''
    # --> Preciso fazer laço ficar rodando mesmo durante o input
    while True:
        print('\x1b[2K\r', end='', flush=True)
        print('\033[1;32m>>\033[0;0m', end='', flush=True)
        sleep(0.5)
        print('\x1b[2K\r', end='  ', flush=True)
        sleep(0.5)
    player1 = input()
    Minha intenção no trecho de código acima era fazer '>>' ficar piscando na tela'''
    
    player1 = input('\033[1;32m>>\033[0;0m ')
    player2 = random(1,3) # [1] é pedra, [2] é papel, [3] é tesoura
   
    sleep(1.5)
    if player1 == '1':
        print('\n\nVocê escolheu: Pedra')
    elif player1 == '2':
        print('\n\nVocê escolheu: Papel')
    elif player1 == '3':
        print('\n\nVocê escolheu: Tesoura')
    else:
        print('Entrada inválida')

    sleep(1.5)
    if player2 == 1:
        print('Computador escolheu: Pedra\n')
    elif player2 == 2:
        print('Computador escolheu: Papel\n')
    elif player2 == 3:
        print('Computador escolheu: Tesoura\n')
    else:
        print('Entrada inválida')



    sleep(1)
    if player1 == '1': # Pedra
        if player2 == 1: #pedra é igual a pedra -> empate
            input('Empate!!\nJogue de novo\n\n\n')
            play()

        if player2 == 2: #pedra é enrolada pelo paper -> perdeu
            print('Você perdeu!!')

        if player2 == 3: #pedra quebra a tesoura -> ganhou
            print('\033[1;32mVocê venceu!!\033[0;0m')


    elif player1 == '2': # Papel
        if player2 == 1: #papel é enrola pedra -> venceu
            print('\033[1;32mVocê venceu!!\033[0;0m')

        if player2 == 2: #papel é igual a papel -> empate
            input('Empate!!\nJogue de novo\n\n\n')
            play()

        if player2 == 3: #papel é cortado por tesoura -> perdeu
            print('Você perdeu!!')


    elif player1 == '3': # Tesoura
        if player2 == 1: #tesoura é quebrada por pedra -> perdeu
            print('Você perdeu!!')

        if player2 == 2: #tesoura corta papel -> venceu
            print('\033[1;32mVocê venceu!!\033[0;0m')

        if player2 == 3: #tesoura é igual a tesoura -> empate
            input('Empate!!\nJogue de novo\n\n\n')
            play()

    sleep(1.5)
    jogar_de_novo = input('\n\nJogar novamente? [S/N]\n\033[1;32m>>\033[0;0m ')
    print('\n\n\n')
    if jogar_de_novo == 's':
        try:
            os.system('cls')
        except:
            os.system('clear')
        play()
    elif jogar_de_novo == 'n':
        exit()
    jogar_de_novo = 0

    player1 = 0
    player2 = 0

play()
