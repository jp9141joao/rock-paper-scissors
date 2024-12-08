import random
import os
import time

def Iniciar(Placar):
    os.system('cls')
    Escolha = int(input(f'\n* Placar *\nVocê: {Placar[0]}\nAdversario: {Placar[1]}\n\n* Escolha *\n1- Pedra\n2- Papel\n3- Tesoura\nR: '))
    while Escolha < 1 and Escolha > 3:
        Escolha = int(input(f'\n* Placar *\nVocê: {Placar[0]}\nAdversario: {Placar[1]}\n\n*Escolha invalida! *\n1- Pedra\n2- Papel\n3- Tesoura\nR: '))

    Adversario = random.randint(1,3)

    if Adversario == 1:
        Resp = 'Pedra'
    elif Adversario == 2:
        Resp = 'Papel'
    else:
        Resp = 'Tesoura'

    print(f'\nAdversario escolheu {Resp}!')
    time.sleep(2)

    if Escolha == Adversario:
        print('\nJogo empatado!')
    elif Escolha == 1 and Adversario == 2:
        print('\nVocê perdeu!')
        Placar[1] += 1 
    elif Escolha == 1 and Adversario ==  3:
        print('\nVocê ganhou!')
        Placar[0] += 1 
    elif Escolha == 2 and Adversario == 1:
        print('\nVocê ganhou!')
        Placar[0] += 1 
    elif Escolha == 2 and Adversario == 3:
        print('\nVocê perdeu!')
        Placar[1] += 1 
    elif Escolha == 3 and Adversario == 1:
        print('\nVocê perdeu!')
        Placar[1] += 1 
    elif Escolha == 3 and Adversario == 2:
        print('\nVocê ganhou!')
        Placar[0] += 1 

    Voltar = int(input('\nDigite "1" para voltar\nR: '))
    while Voltar != 1:
        Voltar = int(input('\nOpção invalida!\nDigite "1" para voltar\nR: '))

Placar = [0,0]

while True:
    os.system('cls')

    Menu = int(input(f'\n* Placar *\nVocê: {Placar[0]}\nAdversario: {Placar[1]}\n\n* Menu *\n1- Começar\n2- Sair\nR: '))
    while Menu != 1 and Menu != 2:
        Menu = int(input('\n* Menu *\nOpção invalida!\n1- Começar\n2- Sair\nR: '))

    if Menu == 1:
        Iniciar(Placar)
    else:
        print('\nPrograma finaliado!')
        break
