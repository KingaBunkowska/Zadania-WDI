import math

def min_cost(chessboard, k, i, suma, sumaMin = math.inf):
    if i + 1 ==len(chessboard) and suma < sumaMin:
        return suma

    if i+1 == len(chessboard):
        return sumaMin

    if suma>sumaMin:
        return math.inf

    if k == 7:
        return min(min_cost(chessboard, k-1, i+1, suma + chessboard[i+1][k-1], sumaMin),
               min_cost(chessboard, k, i+1, suma + chessboard[i+1][k], sumaMin))

    if k == 0:
        return min(min_cost(chessboard, k, i+1, suma + chessboard[i+1][k], sumaMin),
               min_cost(chessboard, k+1, i+1, suma + chessboard[i+1][k+1], sumaMin))


    return min(min_cost(chessboard, k-1, i+1, suma + chessboard[i+1][k-1], sumaMin),
               min_cost(chessboard, k, i+1, suma + chessboard[i+1][k], sumaMin),
               min_cost(chessboard, k+1, i+1, suma + chessboard[i+1][k+1], sumaMin))


T = [[1, 4, 7, 5, 8, 3, 6, 2],
     [9, 0, 4, 3, 7, 3, 1, 7],
     [8, 4, 0, 2, 4, 4, 8, 4],
     [7, 3, 4, 0, 1, 3, 2, 6],
     [3, 5, 0, 3, 3, 3, 3, 3],
     [1, 5, 0, 4, 2, 6, 8, 2],
     [5, 1, 1, 0, 5, 6, 7, 8],
     [9, 9, 9, 9, 1, 3, 3, 3]]

k = 0
print(min_cost(T, k, 0, T[0][k]))