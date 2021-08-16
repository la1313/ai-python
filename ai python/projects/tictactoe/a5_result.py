# Result function and testing
import copy
from a3_player import player

X = "X"
O = "O"
EMPTY = None

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = copy.deepcopy(board)
    # remove raise NotImplementedError statement, add your code
    raise NotImplementedError
    return newboard
    
if __name__ == '__main__':
    board = [[None, X, O],
             [X, X, None],
             [None, O, None]]
    
    action = (1,2)
    newboard = result(board,action)
    ''' Expected Result:
        [None, 'X', 'O']
        ['X', 'X', 'O']
        [None, 'O', None]
    '''
    for i in range(3):
        print(newboard[i]) 