def split(t, i=0, sum_a=0, sum_b=0, sum_c=0):
    if i >= len(t):
        if sum_a == sum_b and sum_b == sum_c:
            return 1
        else:
            return 0

    return split(t, i+1, sum_a + ones(t[i]), sum_b, sum_c) or split(t, i + 1, sum_a, sum_b + ones(t[i]), sum_c) or split(t, i + 1, sum_a, sum_b, sum_c + ones(t[i]))


def ones(a):
    res = 0

    while a > 0:
        res += a%2
        a //= 2

    return res


t = [5, 7, 15]
print(split(t))