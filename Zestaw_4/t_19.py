def correct_products_of_knights(T, N, x, y, k):
    directions = ([-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2])

    result = 0
    for direction in directions:
        i = x + direction[0]
        j = y + direction[1]
        if i>=0 and i<N and j>=0 and j<N:
            if T[x][y] * T[i][j] == k:
                result += 1

    return result


def f(T, N, k):
    result = 0
    for i in range(N):
        for j in range(N):
            result += correct_products_of_knights(T, N, i, j, k)

    return int(result/2) #it is always count twice


N=3
T = [[2, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]

k = 2

print(f(T, N, k))