# Check if the game is finished
# You may need to replace a6_winner with your own file name
from a6_winner import winner 

X = "X"
O = "O"
EMPTY = None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError

if __name__ == '__main__':
    ''' Expected Result
        Test 1 Terminal : True 
        Test 2 Terminal : True
        Test 2 Terminal : False
    '''
    print("Test 1",end=" ")
    board = [[O, X, O],
             [X, X, O],
             [O, X, None]]
    isFinished = terminal(board)
    print(f"Terminal : {isFinished} ")

    print("Test 2",end=" ")
    board = [[O, X, O],
             [X, X, O],
             [O, X, X]]
    isFinished = terminal(board)
    print(f"Terminal : {isFinished} ")

    print("Test 3",end=" ")
    board = [[O, X, O],
             [X, X, O],
             [O, None, X]]
    isFinished = terminal(board)
    print(f"Terminal : {isFinished} ")