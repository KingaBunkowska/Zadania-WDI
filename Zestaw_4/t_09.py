def product_square(T, N, e1i, e1j, e2j):
    size = e2j - e1j
    if e1i + size >= N:
        return -1

    return T[e1i][e1j] * T[e1i][e2j] * T[e1i + size][e1j] * T[e1i + size][e2j]


def center(e1i, e1j, e2j):
    size = e2j - e1j
    i = size//2 + e1j
    j = size//2 + e1i

    return i, j


def find_square(T, N, k):
    for i in range(0, N-2):
        for j in range(0, N-2):
            first_elementI = i
            first_elementJ = j
            for x in range(first_elementJ+2, N, 2):
                second_elementJ = x
                if k == product_square(T, N, first_elementI,first_elementJ, second_elementJ):
                    return center(first_elementI, first_elementJ, second_elementJ)

    return -1

T = [[1, 2, 3, 4],
     [4, 5, 6, 7],
     [1, 8, 1, 0],
     [1, 1, 1, 1]]
k = 24
N = 4
x = find_square(T, N, k)
if x != -1:
    print(x)
else:
    print("Nie udało się znaleźć kwadratu")