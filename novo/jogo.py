import tabuleiro

# by: Arthur Sena e Jackson Douglas

LINHA = ['A','B','C','D','E','F','G','H','I','J']
COLUNA = [1,2,3,4,5,6,7,8,9,10]
i = 0
j = 0
fogo = 'F'
agua = 'A'

# by: Arthur Sena
def passaVez(vez):
    if vez == 1:
        vez = 2
    else:
        vez = 1
    return vez

# by: Jackson Douglas
def mudaCampo(tabuleiro, lin, col, letra):
    tabuleiro[lin][col] = letra

def tiro(jogador, tab, tabPecas):
    print(f'Vez de {jogador}')
    print('\nTabuleiro adversário\n')
    tabuleiro.mostraTabuleiro(tab)
    # by: Arthur Sena
    lin = input('Digite a linha [A-J]: ').upper()
    col = int(input('Digite a coluna [1-10]: '))
    for i in range(len(LINHA)):
        if lin[0] == LINHA[i]:
            x = i
    for j in range(len(COLUNA)):
        if col == COLUNA[j]:
            y = j
    # by: Jackson Douglas
    if tabPecas[x][y] == 'N':
        if tab[x][y] == 'F':
            acerto = 0
            return acerto
        print('FOGO!\n')
        mudaCampo(tab, x, y, fogo)
        acerto = 1
    else:
        print('AGUA!\n')
        mudaCampo(tab, x, y, agua)
        acerto = 0
    return acerto
    
    