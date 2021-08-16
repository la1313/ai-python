# Create terminal function and test it

X = "X"
O = "O"
EMPTY = None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError

if __name__ == '__main__':
    def printwinner(w):
        if w is None:
            print("Tie")
        else:
            print(f"{w} Palyer won.")
    
    ''' Expected Result
        Test 1:X Palyer won.
        Test 2:X Palyer won.
        Test 3:O Palyer won.
        Test 4:Tie
    '''
    print("Test 1",end=":")
    board = [[O, X, O],
             [X, X, O],
             [O, X, X]]
    w = winner(board)
    printwinner(w)

    print("Test 2",end=":")
    board = [[O, X, O],
             [X, X, X],
             [O, O, X]]
    w = winner(board)
    printwinner(w)

    print("Test 3",end=":")
    board = [[O, X, O],
             [X, O, X],
             [X, X, O]]
    w = winner(board)
    printwinner(w)

    print("Test 4",end=":")
    board = [[O, X, X],
             [X, O, O],
             [O, None, X]]
    w = winner(board)
    printwinner(w)