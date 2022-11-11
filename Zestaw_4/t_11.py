def is_friend(a, b):
    A = [0 for _ in range(10)]
    B = [0 for _ in range(10)]

    while a != 0:
        A[a%10] += 1
        a //= 10

    while b != 0:
        B[b%10] += 1
        b //= 10

    for i in range(10):
        if A[i] != B[i]:
            return 0

    return 1


def are_neighbours_friends(i, j, T, N):
    directions = ([0, 1], [1, 0], [0, -1], [-1, 0])
    for x in range(4):
        a = i + directions[x][0]
        b = j + directions[x][1]
        if a < N and b < N and a >= 0 and b >= 0:
            if is_friend(T[a][b], T[i][j]) != 1:
                return 0

    return 1


def f(T, N):
    counter = 0

    for i in range(N):
        for j in range(N):
            if are_neighbours_friends(i, j, T, N):
                print(i,j, T[i][j])
                counter += 1

    return counter

N = 3
T = [[23, 32, 28],
     [32, 82, 28],
     [2, 4, 82]]

print(f(T, N))
