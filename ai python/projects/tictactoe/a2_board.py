# Board state

X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

def printboard(board):
    for i in range(3):
        print(board[i]) 

print(board)

def move(board, action,player):
    i,j = action
    board[i][j] = player
    return board

print("X player")
board[0][1] = X
printboard(board)

print("O player")
board[1][1] = O
printboard(board)

print("X player")
board = move(board,(0,2),X)
printboard(board)




