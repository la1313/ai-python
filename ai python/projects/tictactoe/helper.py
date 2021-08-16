import math

board = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

print(board[2][1])

for i in range(3):
    for j in range(3):
        print(f"({i},{j}) - {board[i][j]}")


board = [[None, "X", "O"],
         ["X", "X", None],
         [None, "O", None]]

'''
1. Is the game over?
2. Who's turn? X player or O player?
'''

board = [["X", "X", "O"],
         ["X", "X", "O"],
         ["O", "O", "X"]]

board = [["O", "X", "X"],
         ["X", "O", "O"],
         ["O", "X", "X"]]
'''
3. Who has Won? or tie
'''

 
a = 2
b = 2
c = 2
if a == b == c == 2:
    print("true")
else:
    print("false")
 