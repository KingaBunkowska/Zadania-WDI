def na_czworkowy(a):
    result = 0
    i = 0
    while a>0:
        result += (a%4) * (10**i)
        i += 1
        a //= 4

    return result


def te_same_cyfry(a, b):
    A = [0 for _ in range(10)]
    B = [0 for _ in range(10)]

    while a>0:
        A[a%10] += 1
        a //= 10

    while b>0:
        B[b%10] += 1
        b //= 10

    for i in range(10):
        if not((A[i]>0 and B[i]>0) or (A[i]==0 and B[i]==0)):
            return 0

    return 1


def f(T, N):
    result = 0
    for i in range(0, N):
        for j in range(0, N):
            if i!=j and te_same_cyfry(na_czworkowy(T[i]), na_czworkowy(T[j])):
                result += 1

    return result


N = 6
T = [13, 23, 33, 57, 107, 18]

print(f(T, N))