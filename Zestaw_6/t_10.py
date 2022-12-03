def wyznacznik(col, act_size, cur_size): # actual size(original)
    if cur_size == 1:
        for row in range(0, act_size):
            if legal_row[row]:
                return m[row][col]

    res = 0
    x = 0
    for row in range(0, act_size):
        if legal_row[row]:
            x += 1
            legal_row[row] = 0
            X = wyznacznik(col+1, act_size, cur_size-1)
            res += m[row][col] * (-1)**(x) * wyznacznik(col+1, act_size, cur_size-1)
            legal_row[row] = 1

    return res


m = [[2, 2, 2, -1, -2],
     [-1, 1, 1, 2, 1],
     [1, 3, 1, -2, -1],
     [2, -1, 5, 3, -1],
     [-1, -2, -1, 1, 1]]

n = len(m)

legal_row = [1 for _ in range(0, n)]

print(wyznacznik(0, n, n))