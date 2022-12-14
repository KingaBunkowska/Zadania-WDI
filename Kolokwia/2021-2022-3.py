import math

def nwd(a, b):
    if a<b:
        a, b = b, a

    while b!=0:
        a, b = b, a%b

    return a


def race(nr_wiezy, t, x=0, y=0, pos_moves=(-1, -1), goal= (-1, -1), no_moves=0):
    if nr_wiezy==2:
        print(x, y)
    n = len(t)
    if no_moves == 0:
        data = ((0, 0, ((0, 1), (1, 0)), (n-1, n-1)), (0, n-1, ((0, -1), (1,  0)), (n-1, 0)))
        x, y, pos_moves, goal = data[nr_wiezy-1]

    if x == goal[0] and y == goal[1]:
        return no_moves

    if no_moves > n * 2 + 1:
        return math.inf

    res = math.inf
    for move in pos_moves:
        tmpx = x + move[0]
        tmpy = y + move[1]
        if tmpx < n and tmpx >= 0 and tmpy >= 0 and tmpy < n and nwd(t[tmpx][tmpy], t[x][y]) == 1:
            tmpres = race(nr_wiezy, t, tmpx, tmpy, pos_moves,goal, no_moves + 1)
            if tmpres < res:
                res = tmpres

    return res


t = [[1, 2, 4, 8],
     [3, 2, 2, 4],
     [4, 2, 2, 2],
     [1, 5, 1, 2]]

wieza1 = race(1, t)
wieza2 = race(2, t)

if wieza2 != math.inf and wieza2<wieza1:
    print(2)
elif wieza1 != math.inf and wieza1<wieza2:
    print(1)
else:
    print("undefined")
