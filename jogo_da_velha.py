from verficar_vitoria import verificar_empate
from verficar_vitoria import verificar_vitoria_x
from verficar_vitoria import verificar_vitoria_o


def menu_jogo():
    print("-------------------------------")
    print("Seja bem-vindo ao jogo da velha!")
    print("-------------------------------")


tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]


def imprimir_jogo_da_velha():
    print(f"{tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("---------")
    print(f"{tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("---------")
    print(f"{tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")


def marcar_tabuleiro():
    jogadas = 0

    while jogadas < 9:
        x_linha, x_coluna = input("É a vez do jogador X, em que posição você deseja jogar? (linha coluna): ").split()
        x_l = int(x_linha)
        x_c = int(x_coluna)
        while tabuleiro[x_l][x_c] != "":
            print("Posição Inválida!")
            x_linha, x_coluna = input("Escolha outra posição válida (linha coluna): ").split()
            x_l = int(x_linha)
            x_c = int(x_coluna)
        tabuleiro[x_l][x_c] = "X"
        imprimir_jogo_da_velha()
        jogadas += 1
        if verificar_vitoria_x(tabuleiro):
            salvar_resultado(tabuleiro)
            print("O jogador X venceu!")
            break
        elif verificar_empate(tabuleiro):
            salvar_resultado(tabuleiro)
            print("O jogo terminou em empate!")
            break
        
        o_linha, o_coluna = input("É a vez do jogador O, em que posição você deseja jogar? (linha coluna): ").split()
        o_l = int(o_linha)
        o_c = int(o_coluna)
        while tabuleiro[o_l][o_c] != "":
            print("Posição Inválida!")
            o_linha, o_coluna = input("Escolha outra posição válida (linha coluna): ").split()
            o_l = int(o_linha)
            o_c = int(o_coluna)
        tabuleiro[o_l][o_c] = "O"
        imprimir_jogo_da_velha()
        jogadas += 1
        
        if verificar_vitoria_o(tabuleiro):
            salvar_resultado(tabuleiro)
            print("O jogador O venceu!")
            break
        elif verificar_empate(tabuleiro):
            salvar_resultado(tabuleiro)
            print("O jogo terminou em empate!")
            break

def salvar_resultado(tabuleiro):
    with open("resultado_jogo.txt", "w") as arquivo:
        for linha in tabuleiro:
            arquivo.write(' | '.join(linha) + '\n')

menu_jogo()
marcar_tabuleiro()
salvar_resultado(tabuleiro)