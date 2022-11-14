def odleglosc_dobra(x, y, a, b):
    return  abs(x-a)>2 and abs(y-b)>2


def sprawdz_sumy(t, u, n):
    res = 0
    for i in range(n):
        res += t[u[i][0]][u[i][1]]

    return res == 0


def f(t, n):
    pozycje_kroli = [[0, 0] for _ in range(n)]
    for z in range(0, n):
        pozycje_kroli = [[0, 0] for _ in range(n)]
        pozycje_kroli[0] = [0, z]
        for i in range(1, n):

            for j in range(n):
                if i == 0:
                    pozycje_kroli[0] = [i, j]
                elif i==1:
                    if odleglosc_dobra(i, j, pozycje_kroli[0][0], pozycje_kroli[0][1]):
                        pozycje_kroli[1]=[i, j]
                else:
                    if odleglosc_dobra(i, j, pozycje_kroli[i-1][0], pozycje_kroli[i-1][1]) and odleglosc_dobra(i, j, pozycje_kroli[i-2][0], pozycje_kroli[i-2][1]):
                        pozycje_kroli[i] = [i, j]

        if sprawdz_sumy(t, pozycje_kroli, n):
            return 1

    return 0



