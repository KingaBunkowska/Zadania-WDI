import math


def sum_of_line(T, x,  y, N, n, mode):
    if mode:
        direction=(1, 0)
        if n+x>N:
            return -math.inf

    else:
        direction = (0, 1)
        if n+y>N:
            return -math.inf


    result = 0
    while n>0:
        result += T[x][y]
        x += direction[0]
        y += direction[1]
        n-=1

    return result

def MaxLine(T, N):
    Max = T[0][0]
    for size in range (1, 11):
        for x in range (N):
            for y in range(N):
                for mode in range(2):
                    current = sum_of_line(T,x, y, N, size, mode)
                    if current>Max:
                        Max = current


    return Max

N= 3
T=[ [2,-92879,4],
    [-2,5,-4],
    [1, -1, 1]]
#print(sum_of_line(T, 2, 2, N, 8, 1))

print(MaxLine(T, N))
