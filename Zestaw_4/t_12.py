import math


def is_composite(a):
    for i in range(2, int(math.sqrt(a))+1):
        if a%i == 0:
            return 1

    return 0

def count_composite_neighbours(x, y, z, N, T):
    counter = 0
    for i in range(3):
        for j in range(3):
            for m in range(3):
                a = x + i
                b = y + j
                c = z + m
                if not(i == j == m == 0) and ((a < N and a>=0) and (b<N and b>=0) and (c<N and c>=0)):
                    if is_composite(T[a][b][c]):
                        counter += 1

    return counter

def f(T, N):
    counter = [0 for _ in range(N)] # Liczy ile tych liczb jest na odpowiednich poziomach

    for a in range(N):
        for b in range(N):
            for c in range(N):
                if count_composite_neighbours(a, b, c, N, T) == 6:
                    counter[a] += 1

    value = counter[0]
    for i in range(1, N):
        if counter[i] != value:
            return 0

    return 1

N=3
T= [[[1,1,1] for _ in range(3)] for _ in range(3)]

print(f(T,N))