def is_compatible_bin(a, b):
    A = [0,0]
    B = [0,0]

    while a!=0:
        A[a%10] += 1
        a //= 10

    while b != 0:
        B[b%10] += 1
        b //= 10

    if A[0] == B[0] and A[1] == B[1]:
        return 1

    return 0


def to_binary(a):
    result = 0
    while a!=0:
        result *=10
        result += a%2
        a //= 2

    return result


def percentage(T, size, i, j):
    result = 0
    for a in range(size):
        for b in range(size):
            result += T[i+a][j+b]

    return result/(size**2)


def f (T1, N1, T2, N2):
    for i in range(N2-N1+1):
        for j in range(N2 - N1 + 1):
            sum = 0
            for a in range (N1):
                for b in range(N1):
                    if is_compatible_bin(to_binary(T1[a][b]), to_binary(T2[a+i][b+j])):
                        sum += 1

            if sum / (N1 ** 2) > 0.33:
                return 1


    return 0


N1= 2
T1 = [[1, 1],
      [1, 1]]

N2= 3
T2 = [[3, 6, 1],
      [8, 1, 1],
      [6, 1, 1]]

print(f(T1, N1, T2, N2))
