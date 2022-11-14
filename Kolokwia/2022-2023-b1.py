def czy_dobry_ciag(t, n, i, j):
    if i!=0 and t[i]>=t[i-1]:
        return 0
    if j!=n-1 and t[j]<=t[j+1]:
        return 0
    if j-i<=1:
        return 0

    for x in range(i, j):
        if t[x]>t[x+1]:
            return 0

    return 1


def dobre(t, i, j, a, b):

    if i == a or j==b:
        return 0
    else:
        if t[i]>=t[b] or t[j]<=t[a]:
            return 1

    return 0



def sequence(t):
    n = len(t)
    for i in range(n):
        for j in range(i+1, n):
            if czy_dobry_ciag(t, n, i, j):
                for a in range(i+1, n):
                    for b in range(a+1, n):
                        if czy_dobry_ciag(t, n, a, b) and dobre(t, i, j, a, b):
                            return 1

    return 0


n = 17
t=[2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]

print(sequence(t)),


