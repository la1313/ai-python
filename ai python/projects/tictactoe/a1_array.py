# Two-demision array

state = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

print(state[0][0])
print(state[2][1])
print(state[2][2])

for i in range(3):
    for j in range(3):
        print(f"({i},{j}) - {state[i][j]}")