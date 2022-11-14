def niebezpieczne(pkt_nieb, x, y, n):
    sasiedzi = ([-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1], [0,0])
    for sasiad in sasiedzi:
        a = x + sasiad[0]
        b = y + sasiad[1]
        if (a>=0 and a<n) and (b>=0 and b<n):
            pkt_nieb[a][b] += 1

    return pkt_nieb


def spr_niebezpiczne(pkt_nieb, x, y, n):
    sasiedzi = ([-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1], [0,0])
    res = 0
    print(x, y)
    for sasiad in sasiedzi:
        a = x + sasiad[0]
        b = y + sasiad[1]
        if (a >= 0 and a < n) and (b >= 0 and b < n):
            if pkt_nieb[a][b] == 1:
                res += 1

    return res

def usun(poz_skoczkow, n):
    punkty_niebezpieczne = [[0 for _ in range(n)] for _ in range(n)]

    for skoczek in poz_skoczkow:
        punkty_niebezpieczne = niebezpieczne(punkty_niebezpieczne, skoczek[0], skoczek[1], n)

    Max = 0
    maxX = 0
    maxY = 0
    for skoczek in poz_skoczkow:
        x = spr_niebezpiczne(punkty_niebezpieczne, skoczek[0], skoczek[1], n)
        if x>Max:
            Max = x
            maxX = skoczek[0]
            maxY = skoczek[1]

    return Max, maxX, maxY, punkty_niebezpieczne


t = [[1, 0], [2, 3], [4, 1], [4,5]]
n = 6
print(usun(t, n))

