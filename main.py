import tabuleiro
import player
import jogo

# inicializa variáveis
maxJogadores = 2
tabJogador1 = []
tabJogador2 = []
tabPecasJog1 = []
tabPecasJog2 = []
nomeJogador1 = ''
nomeJogador2 = ''

# mensagem de inicialização do jogo
player.apresentacao()

# recebe os nomes dos jogadores 1 e 2
for i in range(maxJogadores):
    if i == 0:
        nomeJogador1 = player.nomeJogador(i+1)
    else:
        nomeJogador2 = player.nomeJogador(i+1)

# cria e aloca os tabuleiros dos jogadores
tabJogador1 = tabuleiro.criaTabuleiro(tabJogador1)
tabJogador2 = tabuleiro.criaTabuleiro(tabJogador2)
tabPecasJog1 = tabuleiro.criaTabuleiro(tabPecasJog1)
tabPecasJog2 = tabuleiro.criaTabuleiro(tabPecasJog2)
print(f"Tabuleiro de {nomeJogador1}:")
tabuleiro.mostraTabuleiro(tabJogador1)
print(f"Tabuleiro do {nomeJogador2}:")
tabuleiro.mostraTabuleiro(tabJogador2)

# cria os tabuleiros dos jogadores com os Navios alocados e pergunta se deve mostrá-los
maxNavios = int(input("\nDigite a quantidade máxima de NAVIOS da partida: "))
tabPecasJog1 = tabuleiro.alocaNavios(tabPecasJog1, maxNavios)
tabPecasJog2 = tabuleiro.alocaNavios(tabPecasJog2, maxNavios)
tabuleiro.mostrarNavios(tabPecasJog1, nomeJogador1, tabPecasJog2, nomeJogador2, maxNavios)

# JOGO
print("""\n\n\n
        INICIO DE JOGO
        \n\n\n
        """)
vez = 1
cont1 = 0
cont2 = 0
while cont1 < maxNavios and cont2 < maxNavios:
    if vez == 1:
        acerto = jogo.tiro(nomeJogador1, tabJogador2, tabPecasJog2)
        if acerto == 1:
            cont1 += 1
        else:
            vez = jogo.passaVez(vez)
    else:
        acerto = jogo.tiro(nomeJogador2,tabJogador1, tabPecasJog1)
        if acerto == 1:
            cont2 += 1
        else:
            vez = jogo.passaVez(vez)

if cont1 == maxNavios:
    print(f'\nPARABENS {nomeJogador1}, você VENCEU!')
if cont2 == maxNavios:
    print(f'\nPARABENS {nomeJogador2}, você VENCEU!')

print("""\n\n\n
        FIM DE JOGO
        \n\n\n
        """)