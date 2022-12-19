N = 8
chessboard = [[0 for _ in range(N)] for _ in range(N)]
flag = 0


def print_chessboard():
    for i in range(len(chessboard)):
        print(chessboard[i])


def jump_possible(a, b):
    if a < 0 or b < 0 or a >= N or b >= N:
        return 0
    if chessboard[a][b] != 0:
        return 0
    return 1

def knight(x=0, y=0, i=1):
    global flag
    if flag == 0:

        chessboard[x][y] = i

        if i == N**2:
            print("flaga", x, y, i)
            print_chessboard()
            flag = 1

        directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        for direction in directions:
            a = x + direction[0]
            b = y + direction[1]
            if jump_possible(a, b):
                    knight(a, b, i+1)
                    chessboard[a][b] = 0

        chessboard[x][y] = 0


knight(0, 0)
