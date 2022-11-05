def NWW (a, b, c):
    i = 2
    nww = 1
    while a != 1:
        while a % i == 0:
            a //= i
            nww *= i
            if b % i == 0:
                b //= i

            if c % i == 0:
                c //= i

        i += 1

    i = 2
    while b != 1:
        while b % i == 0:
            b //= i
            nww *= i
            if c % i == 0:
                c //= i

        i += 1

    return nww * c

