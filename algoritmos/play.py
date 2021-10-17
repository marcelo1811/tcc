## where code begins
import numpy as np
from minimax import findBestMove

board = [
    [ '_', '_', '_' ],
    [ '_', '_', '_' ],
    [ '_', '_', '_' ]
]
bestVal = 2

print(np.matrix(board))
while not bestVal in [-10, 10]:
    print("Escolha uma posição para jogar (Você é o 'o')")
    line = int(input("linha:")) - 1
    col = int(input("coluna:")) - 1
    board[line][col] = "o"
    bestMove, bestVal = findBestMove(board)
    board[bestMove[0]][bestMove[1]] = "x"
    print(np.matrix(board))
    if (bestVal == 10):
        print(np.matrix(board))
    elif (bestVal == -10):
        print(np.matrix(board))