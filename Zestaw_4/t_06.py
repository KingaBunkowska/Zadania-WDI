import math

def unique(N, T1, ele):
    one = 0
    for i in range(0, N):
        for j in range(0, N):
            if T1[i][j] == ele and one == 0:
                one = 1
            elif T1[i][j] == ele:
                return 0

    return 1


def end(index, N):
    for i in range(0, N):
        if index[i] < N:
            return 0

    return 1

def f(T1, T2, N):
    index = [0 for _ in range(N)]
    currI2 = 0

    while True:
        jump = 0
        Min = math.inf
        MinI = -1
        for i in range(0, N):

            if index[i] < N:
                value = T1[i][index[i]]
                uniq = unique(N, T1, value)
                if uniq == 1 and value < Min:
                    Min = value
                    MinI = i
                elif uniq == 0:
                    index[i] += 1
                    jump = 1

        if end(index, N):
            return T2
        elif MinI != -1 and jump == 0:
            T2[currI2] = Min
            index[MinI] += 1
            currI2 += 1


T1 = [[1, 2, 3], [2, 3, 4], [6, 8, 9]]
T2 = [0 for _ in range(3 * 3)]

print(f(T1, T2, 3))
