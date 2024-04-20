  <h1 align="center"> Jogo da Velha </h1>
  
  
  <p align="center">
    <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;
       <a href="#-projeto-2">Projeto 2</a>&nbsp;&nbsp;&nbsp;
  
  
  ## 💻 Projeto
  
  O objetivo desta atividade é criar um programa que escreva um tabuleiro de jogo da velha que irá ser alterado a medida que as jogadas são feitas. O tabuleiro deve sempre ser salvo em um arquivo.
  
  1. Escreva uma função que exiba na tela o menu inicial de um jogo da velha, o seu menu deve dar as boas vindas aos jogadores, exemplo:
  ----------------------------------
  Seja bem-vindo ao jogo da velha!
  
  ----------------------------------
  2. Considere que o seu programa terá uma representação do tabuleiro do jogo da velha como uma matriz 3x3, onde cada espaço do tabuleiro começa com " " uma string vazia. Esse tabuleiro será uma variável global, compartilhada entre todo o programa. Construa uma função para imprimir na tela o tabuleiro do jogo da velha de forma similar ao que escrevemos no papel.
  3. Seu programa terá dois jogadores, o jogador X e o jogador O. Após exibir o menu de boas vindas, seu programa deve pedir que o jogador X escreva em qual posição do tabuleiro o jogador quer marcar. Abaixo, um exemplo de como será a informação de entrada:
  É a vez do jogador X, em qual posição você deseja jogar?
  > 0 0
  4. Com isso, seu programa deve acessar o tabuleiro e marcar o caracter "X" na posição tabuleiro[0][0]. É recomendado criar uma função marca_posicao(jogador, linha, coluna) essa função receberá copmo parâmetro o simbolo do jogador que irá marcar no tabuleiro, qual a posição da linha e da coluna, com esses parâmetros, a função deverá marcar na variável tabuleiro o simbolo do jogador em questão.Ao finalizar a jogada do jogador X, seu programa deve imprimir o tabuleiro atualizado na tela pedir que o jogador O insira a posição que ele deseja jogar.
  5. Altere a sua função de marcar a posição para que ela não permita que o jogador marque sua jogada em uma posição que já está ocupada no tabuleiro. Quando isso acontecer, seu programa deverá informar que a posição é inválida e pedir que o jogador informe uma nova posição válida. O programa não deve avançar enquanto a posição válida não for inserida.
  6. Toda vez que o tabuleiro for alterado, seu programa deverá escrever em um arquivo 'tabuleiro.txt' o estado do tabuleiro depois de cada jogada. O formato do arquivo gerado deve ser como o exemplo abaixo:<br>
  X| |X<br>
  X|O|O<br>
  X|O|X
  
  ## 💻 Projeto 2
  Faça um programa que leia um arquivo no formato padrão exibido pela professora. O arquivo é um tabuleiro de jogo da velha e seu programa deve informar quem ganhou o jogo ou se houve empate.

Exemplo do Arquivo:<br>
X| |X<br>
X|O|O<br>
X|O|X

O arquivo sempre terá 5 linhas; as linhas 2 e 4 sempre serão tracejados; Só podem ter os caracteres X, O, | ou espaço vazio em cada posição do arquivo.


Obs: Esse projeto foi posteriormente substituído para ser a função que verifica a vitória do Jogo da velha.
  
  
  
  
  
   ## 🚀 Tecnologias
  
  Esse projeto foi desenvolvido com as seguintes tecnologias:
  
  - Python 
  - Git e Github
