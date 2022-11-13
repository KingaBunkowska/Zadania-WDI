def sum_tower(x, y, T, N):
    result = 0

    for i in range(N):
        result += T[i][y] + T[x][i]

    return result - T[x][y] - T[x][y]


def f(T, N):
    Max1 = -1
    Max2 = -1
    i1 = i2 = j1 = j2 = 0
    for i in range(N):
        for j in range(N):
            current = sum_tower(i, j, T, N)
            if current>Max1:
                Max1, Max2 = current, Max1
                i1, j1, i2, j2 = i, j, i1, i2
            elif current>Max2:
                Max2 = current
                i2, j2 = i, j

    return i1, j1, i2, j2


N= 3
T=[[1, 2, 5],
   [1, 1, 3],
   [1, 4, 1]]

print(f(T, N))