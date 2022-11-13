def sum_of_neighbours(T, N, x, y):
    neighbours = ([1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1])
    result = 0
    for neighbour in neighbours:
        i = neighbour[0]+x
        j = neighbour[1] + y

        if i<N and i>=0 and j>=0 and j<N:
            result += T[i][j]

    return result


def f(T, N):
    Max = sum_of_neighbours(T, N, 0, 0)
    MaxRow = 0
    MaxCol = 0

    for row in range(N):
        for col in range(N):
            current = sum_of_neighbours(T,N, row, col)
            if current > Max:
                Max = current
                MaxRow = row
                MaxCol = col


    return MaxRow, MaxCol


N = 3
T = [[1,1,4],
     [1,89,1],
     [1,1,13]]

print(f(T,N))