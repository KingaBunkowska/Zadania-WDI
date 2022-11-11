def all_1(T, N):
    for i in range(N):
        if T[i]==0:
            return 0

    return 1

def f(T, N):
    Col = [0 for _ in range(N)]
    Row = [0 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if T[i][j] == 0:
                Col[i] = 1
                Row[j] = 1

    return all_1(Col, N) and all_1(Row, N)

T = [[1, 1, 0],
     [0, 1, 1],
     [1, 1, 1]]
N=3

print(f(T, 3))