# nwd(a,b,c) = nwd(nwd(a,b),c) - solution "too easy"
def NWD(a, b, c):

    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a

    while b != 0:
        a, b, c = b, a % b, a % c
        if b == 0 and c != 0:
            b = c

    return a



