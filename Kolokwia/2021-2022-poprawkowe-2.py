def nachodza(a, b):
     return (a[0]>=b[0] and a[1]<=b[1]) or (a[0]<=b[0] and a[1]>=b[0])


def dl(odc):
    return abs(odc[1]-odc[0])


def czy_sie_da(odcinki, n, k, i, pop, znalezione):
    if znalezione == 1:
        return 1
    if k == 0:
        znalezione = 1
    if i>n-1:
        return znalezione
    else:
        print("bez ", i, k)
        czy_sie_da(odcinki, n, k, i+1, pop, znalezione)
        k = k - dl(odcinki[i])
        if k == 0:
            znalezione = 1
        print("z", i, k)
        czy_sie_da(odcinki, n, k, i+1, odcinki[i], znalezione)
        return znalezione




def f(odcinki):
    n = len(odcinki)
    k = 2020
    return czy_sie_da(odcinki, n, k, 0, [-1, -1], 0)


odcinki = [[0, 1], [3, 2137], [0, 2020]]
print(f(odcinki))
