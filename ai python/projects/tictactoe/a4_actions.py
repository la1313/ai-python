# Get all possible actions

X = "X"
O = "O"
EMPTY = None

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


if __name__ == '__main__':
    print("Test 1")
    # Expected Result
    # [(0, 0), (1, 2), (2, 0), (2, 2)]
    board = [[EMPTY, X, O],
            [X, X, EMPTY],
            [EMPTY, O, EMPTY]]
    possible_actions = actions(board)
    print(possible_actions)

    print("Test 2")
    # Expected Result
    # [(2, 2)]
    board = [[O, X, O],
             [X, X, O],
             [X, O, EMPTY]]
    possible_actions = actions(board)
    print(possible_actions)