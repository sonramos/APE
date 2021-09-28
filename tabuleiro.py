import random

# by: Cayo Bruno e Jackson Douglas
def mostraTabuleiro(tabuleiro):
    linhas = ['A','B','C','D','E','F','G','H','I','J'] # vetor que representa as linhas do tabuleiro [A-J]
    for i in range(10): # laço FOR para imprimir os números das colunas do tabuleiro [1-10]
        print(i+1, end=' ') 
    print()
    for i in range(10):
        for j in range(10):
            print(tabuleiro[i][j], end = ' ')
        print(linhas[i])

# by: Cayo Bruno
def criaTabuleiro(tabuleiro):
    #cria tabuleiro para guardar as posições dos navios
    for i in range(10): #Loop FOR 
        linha1 = [] # cria um vetor
        for j in range(10):
            linha1.append("*") # adiciona 'a' (água) ao final do vetor
        tabuleiro.append(linha1) # adiciona o vetor 'linha1' ao vetor 'jogador 1'
    return tabuleiro

# by: Cayo Bruno e Thalyson Demetrio
def alocaNavios(tabuleiro, maxNavios):
    # Inicializa variáveis
    nNavios = 0 #contador de navios posicionados
    x1 = 0
    y1 = 0
    # Posiciona os Navios no tabuleiro
    while nNavios < maxNavios:

# by: Thalyson Demetrio       
        x = random.randint(0,9) # gera número aleatório de 0-9 que será o índice da posição
        y = random.randint(0,9)

        if tabuleiro[x][y] == "*": # checa se a posição está vazia

            if x == 0 and y == 0: # se a posição for a posição [0,0] da matriz
                qq = 4 # contador da checagem
                for i in range(2):
                    for j in range(2):
                        if tabuleiro[x+i][y+j] == "*": # checa se a posição [x+i][y+j] está vazia
                            qq -= 1
                if qq == 0: # Se não houver navios ao redor, adiciona navio na posição [0,0]
                    tabuleiro[x][y] = "N"
                    nNavios += 1
        
            if x == 0 and y == 9: # checa a posição [0,9] da matriz
                qq = 4
                for i in range(2):
                    for j in range(2):
                        if tabuleiro[x+i][y-j] == "*":
                            qq -= 1
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1

            if x == 9 and y == 0: # checa a posição [9,0] da matriz
                qq = 4
                for i in range(2):
                    for j in range(2):
                        if tabuleiro[x-i][y+j] == "*":
                            qq -= 1
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1

            if x == 9 and y == 9: # checa a posição [9,9] da matriz
                qq = 4
                for i in range(2):
                    for j in range(2):
                        if tabuleiro[x-i][y-j] == "*":
                            qq -= 1
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1
# by: Cayo Bruno      
            if x > 0 and x < 9 and y == 0: # se a posição for na lateral esquerda
                qq = 6
                x1 = x - 1 # seleciona posição acima da posição 'x'
                for i in range(3):
                    for j in range(2):
                        if tabuleiro[x1+i][y+j] == "*": # checa acima e na lateral direita
                            qq -= 1
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1

            if x > 0 and x < 9 and y == 9: # se a posição for na lateral direita
                qq = 6
                x1 = x - 1
                for i in range(3): # checa acima da posição
                    for j in range(2):
                        if tabuleiro[x1+i][y-j] == "*": # checa acima e na lateral esquerda
                            qq -= 1
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1
            if x == 0 and y > 0 and y < 9: # se a posição for no topo
                qq = 6
                y1 = y - 1 # seleciona posição antes da posição 'x'
                for i in range(3):
                    for j in range(2):
                        if tabuleiro[x+j][y1+i] == "*":
                            qq -= 1
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1

            if x == 9 and y > 0 and y < 9: # se a posição for no fundo
                qq = 6
                y1 = y - 1
                for i in range(3):
                    for j in range(2):
                        if tabuleiro[x-j][y1+i] == "*":
                            qq -= 1 
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1
            
            if x > 0 and x < 9 and y > 0 and y < 9: # no meião
                qq = 9
                x1 = x - 1
                y1 = y - 1
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[x1+i][y1+j] == "*":
                            qq -= 1
                if qq == 0:
                    tabuleiro[x][y] = "N"
                    nNavios += 1
    return tabuleiro

# by: Jackson Douglas
def mostrarNavios(tab1, nome1, tab2, nome2, navios):
    show = 0
    while show != 1:
        mostrarPreenchido = input(f'Deseja visualizar o tabuleiro preenchido por {navios} Navios? [S/N]: ' ).upper()
        if mostrarPreenchido == 'S':
            print(f"Tabuleiro de {nome1}:")
            mostraTabuleiro(tab1)
            print(f"Tabuleiro do {nome2}:")
            mostraTabuleiro(tab2)
            show = 1
        elif mostrarPreenchido == 'N':
            show = 1
        else:
            print('Opção inválida! Tente novamente.')