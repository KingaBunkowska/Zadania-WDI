def zad(t, k,i=0, s1=0, s2=0, n1=0, n2=0):
    if 2 * k > len(t):
        return 0

    if i>= len(t):
        return s1 == s2 and n1 == k and n2 == k

    return zad(t, k, i + 1, s1 + t[i], s2,  n1 + 1, n2) or zad(t, k, i + 1, s1, s2, n1, n2) or zad(t, k, i + 1, s1, s2 + t[i], n1, n2 + 1)


t = [1, 2, 3, 4, 5]
k = 2
print(zad(t, k))

