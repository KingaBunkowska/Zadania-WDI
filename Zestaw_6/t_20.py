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


def king(x, y, goalx=0, goaly=0, code = 0):
    dirs = ((1, 0), (1, 1), (1, -1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1))

    global flag
    if flag != 0:
        return flag

    if x == goalx and y == goaly:
        flag = code
        return code

    res = 0

    for i in range(8):
        new_x = x + dirs[i][0]
        new_y = y + dirs[i][1]

        if (last_digit(x, y)<first_digit(new_x, new_y)) and (((x > goalx and new_x <= x) or (x < goalx and new_x >= x) or (x == goalx and new_x == goalx)) and ((y>goaly and new_y <= y) or (y < goaly and new_y >= y) or (y == goaly and new_y == y))):
            res += king(new_x, new_y, goalx, goaly, code * 10 + i)
        elif i == 7 and res == 0:
            return 0

    return flag


def to_list(a):
    t = []
    while a>0:
        t.append(a%10)
        a //= 10

    t.reverse()
    return t


chessboard[0][0] = 2
chessboard[0][1] = chessboard[1][0] = 1
flag = 0
print(to_list(king(1, 1, 0, 0)))