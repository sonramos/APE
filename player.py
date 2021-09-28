# Apresentar jogo e Desenvolvedores
def apresentacao():
    print("""Seja bem vindx\n'
            Você está prestes a jogar Batalha Naval.\n
            Um dos melhores jogos que você já viu!\n
            Batalha Naval é um jogo de tabuleiro em que dois jogadores têm de adivinhar\n
            onde estão localizados os navios do oponente.\n
            Existem dois modos de jogo:\n
            [1]-Básico - 10 Navios por jogador.\n
            [2]-Avançado - 10 Navios, 3 Submarinos e 1 Porta aviões por jogador.\n\n
            Designed by: Arthur Sena, Cayo Bruno, Jackson Douglas e Thalyson Demetrio.\n\n""")

# Lê nome do jogador
def nomeJogador(x):
    nome = input(f'Qual o nome do JOGADOR {x}? ').upper()
    return nome

#-------------- PARA IMPLEMENTAÇÃO FUTURA --------------#

# Define qual o modo de jogo será utilizado
#def escolheModo():
#    aux = 1
#    while(aux == 1):
#        print('[1]-Básico\n[2]-Avançado')
#        modo = input('Qual o nível do jogo ([1] ou [2])?\n')
#        if modo == '1':
#            print(f"Modo [{modo}]-Básico selecionado.")
#            aux = 0
#        elif modo == '2':
#            print(f"Modo [{modo}]-Avançado selecionado.")
#            aux = 0
#        else:
#            print("Modo inválido! Por favor, tente novamente.")
#    return modo
