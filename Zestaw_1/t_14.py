def szereg_Mackauriona(x, e):
    result = 0
    i = 0
    while i <= e:
        if i % 2 == 1:
            result += x ** i

        if i % 2 == 3:
            result -= x ** i

        i += 1

    return result
