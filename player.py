# Apresentar jogo e Desenvolvedores
def apresentacao():
    print('Seja bem vindx\n'
            'Você está prestes a jogar o Batalha Naval.\n'
            'Um dos melhores jogos que você já viu!\n'
            'O objetivo do jogo é encontrar e destruir a frota do seu adversário.\n'
            'Existem dois modos de jogo:\n'
            '[1]-Básico - 10 Navios por jogador.\n'
            '[2]-Avançado - 10 Navios, 3 Submarinos e 1 Porta aviões por jogador.\n'
            '\n\nDesigned by: Arthur Sena, Jackson Douglas e Thalyson Demetrio.\n')

# Define qual o modo de jogo será utilizado
def escolheModo():
    aux = 1
    while(aux == 1):
        modo = input('Qual o nível do jogo (1 ou 2)?\n'
                '[1]-Básico\n'
                '[2]-Avançado\n')
        if modo == '1':
            print(f"Modo [{modo}]-Básico selecionado.")
            aux = 0
        elif modo == '2':
            print(f"Modo [{modo}]-Avançado selecionado.")
            aux = 0
        else:
            print("Modo inválido! Por favor, tente novamente.")
    return modo


# Linhas de teste
#apresentacao()
#escolheModo()
