def make_list(a, b, T, N):
    R = []
    while a < N and b < N:
        R.append(T[a][b])
        a += 1
        b += 1

    return R


def geometric_sequence(T, N):
    size = 2
    MaxSize = 2
    first = T[0]
    q = T[1] / T[0]
    for i in range(2, N):
        if T[i]/T[i-1] == q:
            size += 1
        else:
            if size > MaxSize:
                MaxSize = size

            first = T[i-1]
            size = 2
            q = T[i-1]/T[i]

    if size > MaxSize:
        MaxSize = size

    print(T, MaxSize)
    return MaxSize

def f(T, N):
    Max = 2
    for i in range(0, N-2):
        pom = geometric_sequence(make_list(0, i, T, N), len(make_list(0, i, T, N)))
        if pom > Max:
            Max = pom

    for i in range(1, N-2):
        pom = geometric_sequence(make_list(0, i, T, N), len(make_list(0, i, T, N)))
        if pom > Max:
            Max = pom

    return (Max>2, Max)


T = [[2, 2, 4, 6], [1, 4, 4, 6], [1, 2, 8, 8], [1, 2, 4, 16]]
print(f(T, 4))