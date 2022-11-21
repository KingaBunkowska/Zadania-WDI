def wage(number):
    x = 0
    pop = 0
    for i in range(2, number):
        while number % i == 0:
            if pop != i:
                x += 1
            pop = i
            number //= i

    return x


def R(T, i=0, s1 = 0, s2 = 0, s3 = 0):
    if i == len(T) and s1 == s2 and s2 == s3:
        return 1
    if i == len(T):
        return 0

    return R(T, i+1, s1+wage(T[i]), s2, s3) or R(T, i+1, s1, s2 + wage(T[i]), s3) or R(T, i+1, s1, s2, s3 + wage(T[i]))


T = [2, 1, 6, 2, 2, 6, 1]
print(R(T))