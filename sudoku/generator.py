import random

n = 4
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(n):
    values = set([i for i in range(1, n+1)])
    for j in range(n):
        # col = [board[k][j] for k in range(n)]
        # print(col, i, j)
        b = random.sample(values, 1)
        # while b in col:
        #     b = random.sample(values, 1)
        values -= set(b)
        board[i][j] = b[0]
print(board)
