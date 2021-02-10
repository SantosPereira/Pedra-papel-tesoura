from random import randint as random
from time import sleep
#from pisca import pisca


sleep(1)
print('''\n\n\n
▒█▀▀█ █▀▀ █▀▀▄ █▀▀█ █▀▀█ ░░ 　 ▒█▀▀█ █▀▀█ █▀▀█ █▀▀ █░░ 　 █▀▀█ █░░█ 　 ▀▀█▀▀ █▀▀ █▀▀ █▀▀█ █░░█ █▀▀█ █▀▀█ 
▒█▄▄█ █▀▀ █░░█ █▄▄▀ █▄▄█ ▄▄ 　 ▒█▄▄█ █▄▄█ █░░█ █▀▀ █░░ 　 █░░█ █░░█ 　 ░▒█░░ █▀▀ ▀▀█ █░░█ █░░█ █▄▄▀ █▄▄█ 
▒█░░░ ▀▀▀ ▀▀▀░ ▀░▀▀ ▀░░▀ ░█ 　 ▒█░░░ ▀░░▀ █▀▀▀ ▀▀▀ ▀▀▀ 　 ▀▀▀▀ ░▀▀▀ 　 ░▒█░░ ▀▀▀ ▀▀▀ ▀▀▀▀ ░▀▀▀ ▀░▀▀ ▀░░▀ 

▀█░█▀ ▄█░ ░ █▀▀█ 
░█▄█░ ░█░ ▄ █▄▀█ 
░░▀░░ ▄█▄ █ █▄▄█\n\n''')
sleep(1.5)




def play():
    print('Escolha:\n[1] Para Pedra\n[2] Para Papel\n[3] Para Tesoura\n\n\n\n')
    sleep(1)
    
########         fica rodando infinitamente      ----     Provisório
#   while True:   
#       print('\033[1;32m>>\033[0;0m', end='', flush=True)
#       sleep(0.5)
#       print('\x1b[2K\r', end='', flush=True)
#       sleep(0.5)
#######################################################################################

#### Minha intenção no trecho de código acima era fazer '>>' ficar piscando na tela e quando fosse digitado algo no input ele ler a entrada, porém o input para o programa

    player1 = input('\033[1;32m>>\033[0;0m')
    player2 = random(1,3) ### [1] é pedra, [2] é papel, [3] é tesoura
   

    if player1 == '1':
        input('\n\nVocê escolheu: Pedra')
    elif player1 == '2':
        input('\n\nVocê escolheu: Papel')
    elif player1 == '3':
        input('\n\nVocê escolheu: Tesoura')
    else:
        print('Entrada inválida')

    if player2 == 1:
        input('Computador escolheu: Pedra\n')
    elif player2 == 2:
        input('Computador escolheu: Papel\n')
    elif player2 == 3:
        input('Computador escolheu: Tesoura\n')
    else:
        print('Entrada inválida')




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

    
    jogar_de_novo = input('\n\nJogar novamente? [S/N]\n\033[1;32m>>\033[0;0m')
    print('\n\n\n')
    if jogar_de_novo == 's':
        play()
    elif jogar_de_novo == 'n':
        exit()
    jogar_de_novo = 0

    player1 = 0
    player2 = 0

play()
