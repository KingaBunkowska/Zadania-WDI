def possible_queen(row, col, n=8):
    global chessboard
    dirs = ((1, 1), (-1, 1), (-1, -1), (1, -1))

    for i in range(0, n):
        if chessboard[row][i] or chessboard[i][col]:
            return 0

        for dir in dirs:
            x = row + i * dir[0]
            y = col + i * dir[1]
            if x >= 0 and x < n and y>=0 and y < n:
                if chessboard[x][y]:
                    return 0

    return 1


def queen(row=0, n=8):
    global chessboard
    res = 0
    if row == n:
        return 1

    for col in range(n):
        if possible_queen(row, col, n):
            chessboard[row][col] = 1
            res += queen(row+1, n)
            chessboard[row][col] = 0

    return res





n = 8
chessboard=[[0 for _ in range(0, n)] for _ in range(0, n)]

print(queen(0, n))