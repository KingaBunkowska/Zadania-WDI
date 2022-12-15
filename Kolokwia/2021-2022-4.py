def fib(a, n):
    i = j = 1

    while i < a:
        i, j = j, i+j

    if i == a:
        res = [0 for _ in range(2 * n - 1)]
        x , y = i, j
        l = n - 2
        p = n
        res[n - 1] = i

        for it in range(n-1):
            i, j = j, i+j
            x, y = y-x, x
            res[l] = x
            res[p] = i
            l -= 1
            p += 1

        return res
    else:
        return 0

def find_in_list(t):
    res = 0
    for i in range(len(t)):
        res = find_fib(t, i, 0)
        if type(res) == list:
            return res
        res = find_fib(t, i, 1)
        if type(res) == list:
            return res

    return -1


def find_fib(t, i, mode):
    dirs = ((1, 0), (1, 0))
    pos = ((0, i), (i, 0))
    dir = dirs[mode]
    x, y = pos[mode]
    fib_found = 0
    res = []
    list_searches_cor = 0
    while x < len(t) and y < len(t):
        if fib_found == 0:
            list_fib = fib(t[x][y], len(t))
            if type(list_fib) == list:
                fib_found = 1
                list_searches_cor = 1
                res.append(t[x][y])
                rosnacy = malejacy = 1
        else:
            if rosnacy and t[x][y] == list_fib[len(t) - 1 + list_searches_cor]:
                list_searches_cor += 1
                res.append(t[x][y])
                malejacy = 0

            if malejacy and t[x][y] == list_fib[len(t) - 1 - list_searches_cor]:
                list_searches_cor += 1
                res.append(t[x][y])
                rosnacy = 0



        x += dir[0]
        y += dir[1]

    if list_searches_cor >= 3:
        return res
    else:
        return 0



t = [[5, 8, 9],
     [3, 1, 1],
     [2, 0, 1]]

print(find_in_list(t))