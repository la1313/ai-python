# Who's the next player

X = "X"
O = "O"
EMPTY = None

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    raise NotImplementedError

if __name__ == '__main__':
    board = [[EMPTY, X, O],
             [EMPTY, X, EMPTY],
             [EMPTY, O, EMPTY]]
    #It should output X
    print(player(board))

    board = [[EMPTY, X, O],
             [EMPTY, X, X],
             [EMPTY, O, EMPTY]]
    #It should output O
    print(player(board))