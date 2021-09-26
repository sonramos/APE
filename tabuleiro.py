def apresentacao():
    print('Seja bem vindx\n'
            'Você está prestes a jogar o Batalha Naval\n'
            'Um dos melhores jogos que você já viu!\n'
            'O objetivo do jogo é encontrar e destruir a frota do seu adversário\n'
            'Designed by: Arthur Sena, Jackson Douglas e Thalyson Demetrio\n')
def criaTabuleiro(ordem):
    tabuleiro = [[None]*ordem for i in range(ordem)]
    for i in range(ordem):
        for j in range(ordem):
            tabuleiro[i][j] = '*'
    return tabuleiro

def mostraTabuleiro(tabuleiro):
    for i in range(len(tabuleiro)):
        print(f"{tabuleiro[i]}\n")
