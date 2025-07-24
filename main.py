# Bibliotecas: os vou usar para conseguir limpar o terminal e não ficar muita oicsa junta confundiondo o usuario; random vai ser usado para fazer a escolhar aleatoria do computador.

import os
from random import choice
from time import sleep

alternativas = ['pedra', 'papel', 'tesoura']
alternativas_contra_usuario = {'1': 'pedra', '2': 'papel', '3': 'tesoura'}
vitoria = {
    'pedra': 'tesoura',
    'papel': 'pedra',
    'tesoura': 'papel',
}

# Achei importante colocar esse def porque consegui fazer com que ele funcine em todos os simtemas operacionais.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Tentei usar o dicionar que aprendi a pouco tempo em fez de uma longa estrutura de if e elifs.
def obter_escolha_usuario():
    while True:
        print('\033[1;49;33m=-'*30 + '=\033[0m')
        print('Olá, escolha uma das opções abaixo para jogar:\n[1] Pedra\n[2] Papel\n[3] Tesoura')
        escolha_usuario = str(input('Digite aqui >>> ')).lower()

        if escolha_usuario in alternativas_contra_usuario:
            return alternativas_contra_usuario[escolha_usuario]
        
        else:
            limpar_tela()
            print('\033[1;49;31mOpção invàlida. Tente novamente\033[0m')
            sleep(3)
            limpar_tela()

# Parte "Grafica" do jogo.
def jogo():
    usuario = obter_escolha_usuario()
    computador = choice(alternativas)

    print('\033[1;49;33m=-'*30 + '=\033[0m')
    print(f'Você escolheu {usuario} e o computador escolheu {computador}.')

    if usuario == computador:
        print('Resultado: \033[1;49;34mEmpate!\033[0m')
        return 'empate'
    
    elif vitoria[usuario] == computador:
        print('Resultado: \033[1;49;32mVocê ganhou!\033[0m')
        return 'vitoria'

    else:
        print('Resultado: \033[1;49;31mVocê perdeu!\033[0m')
        return 'derrota'

# Esse while eu tinha esquecido como faz então foi bem chatinho de fazer com que ele não parasse do nada.
def completo():
    usuario_vitorias = 0
    usuario_derrotas = 0
    usuario_empates = 0
    while True:
        limpar_tela()
        resultado = jogo()

        if resultado == 'vitoria':
            usuario_vitorias +=1
        
        elif resultado == 'derrota':
            usuario_derrotas += 1
        
        else:
            usuario_empates += 1

        print('\033[1;49;33m=-'*30 + '=\033[0m')
        print(f'Sua pontuação atual é de: {usuario_vitorias} vitórias, {usuario_derrotas} derrotas e {usuario_empates} empates.')
        print('\033[1;49;33m=-'*30 + '=\033[0m')
        recomecar = input("Deseja jogar novamente? (s/n): ").strip().lower()

        if recomecar != 's':
            print('Obrigado e até a próxima!')
            break

completo()