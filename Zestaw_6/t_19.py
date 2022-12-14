#copied t_18.py because it already met conditions (even more, it could find a way to any chequer)

chessboard = [[0 for _ in range(8)] for _ in range(8)]


def first_digit(x, y):
    cur = chessboard[x][y]%10
    pop = 0
    while cur>0:
        pop = cur
        cur //= 10

    return pop


def last_digit(x, y):
    return chessboard[x][y]%10


def king(x, y, goalx=0, goaly=0):
    dirs = ((1, 0), (1, 1), (1, -1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1))

    if x == goalx and y == goaly:
        return 1

    res = 0

    for dir in dirs:
        new_x = x + dir[0]
        new_y = y + dir[1]

        if (last_digit(x, y)<first_digit(new_x, new_y)) and (((x > goalx and new_x <= x) or (x < goalx and new_x >= x) or (x == goalx and new_x == goalx)) and ((y>goaly and new_y <= y) or (y < goaly and new_y >= y) or (y == goaly and new_y == y))):
            res += king(new_x, new_y, goalx, goaly)
        elif dir == (0, -1) and res == 0:
            return 0

    return 1


chessboard[0][0] = 1
print(king(1, 1, 0, 0))