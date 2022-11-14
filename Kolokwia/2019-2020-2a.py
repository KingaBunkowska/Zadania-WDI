def na_dwojkowy(a):
    i = 0
    res = 0
    while a>0:
        res += (a % 2) * (10**i)
        i+=1

        a //= 2

    return res


def nieparzyste_1 (a):
    ile_1 = 0
    while a>0:
        if a%2:
            ile_1 += 1

        a //= 10

    return ile_1%2


def f(t, n):

    for x in range(0, n):
        for y in range(0, n):
            for z in range(0, n):
                dziala = 0
                if y != z:
                    dziala = 1
                    for i in range(0, n):
                        for j in range(0, n):
                            if not(nieparzyste_1(na_dwojkowy(t[i][j]))) and i!=x and j!=y and j!=z:
                                dziala = 0

                if dziala == 1:
                    return 1

    return 0

t = [[0, 1, 0],
     [0, 0, 0],
     [0, 1, 0]]
n= 3

print(f(t, n))


