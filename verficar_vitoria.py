def verificar_vitoria_x(tabuleiro):
    for linha in tabuleiro:
        if linha.count('X') == 3:
            return True

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'X':
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'X':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
        return True

    return False

def verificar_vitoria_o(tabuleiro):
    for linha in tabuleiro:
        if linha.count('O') == 3:
            return True

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == 'O':
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'O':
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if '' in linha:
            return False  
    return True  