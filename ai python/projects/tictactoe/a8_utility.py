# Utility function to evaluate result
# You may need to replace a6_winner with your own file name
from a6_winner import winner

X = "X"
O = "O"
EMPTY = None

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError

if __name__ == '__main__':
    ''' Expected Result
        Test 1 Utility : 1 
        Test 2 Utility : -1 
        Test 3 Utility : 0
    '''
    print("Test 1",end=" ")
    board = [[O, X, O],
            [X, X, O],
            [O, X, None]]

    ut = utility(board)
    print(f"Utility : {ut} ")

    print("Test 2",end=" ")
    board = [[O, X, O],
            [X, O, X],
            [O, X, X]]

    ut = utility(board)
    print(f"Utility : {ut} ")

    print("Test 3",end=" ")
    board = [[X, O, X],
            [X, O, O],
            [O, X, X]]

    ut = utility(board)
    print(f"Utility : {ut} ")