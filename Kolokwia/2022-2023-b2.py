def iloczyn(a, b, x, y, size, t):
    c = size + a -1
    d = b
    w = size + a - 1
    z = y

    return t[a][b] * t[c][d] * t[x][y] * t[w][z]


def rozklad_2_rozne(a):
    czyn1 = czyn2 = 1
    for i in range(2, a):
        while a%i==0:
            if czyn1==1 or czyn1==i:
                czyn1=i
            elif czyn2==1 or czyn2==i:
                czyn2 = i
            else:
                return 0

            a//=i

    return 1


def square(t):
    n = len(t)

    for size in range(2, n):
        for a in range(0, n-size+1):
            x = a
            for b in range(0, n-size+1):
                y = a+size-1
                if rozklad_2_rozne(iloczyn(a, b, x, y, size, t)) and (a!=x or b!=y):
                    return size

    return 0


t = [[21, 24, 99],
    [1, 2, 5],
    [9, 20, 10]]

print(square(t))