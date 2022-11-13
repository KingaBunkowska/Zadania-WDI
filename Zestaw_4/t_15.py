def f(T, N):
    prime_digits = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0]
    for row in range(N):
        all_exist = 1
        if all_exist == 1:
            for col in range(N):
                exist = 0
                while T[row][col] != 0 and exist == 0:
                    T[row][col] //= 10
                    if prime_digits[T[row][col] % 10]:
                        exist = 1
                        #print(T[row][col])

                if exist == 0:
                    all_exist = 0

        else:
            return 0

    return 1



N=3
T=[[1, 2,3],
   [22, 36, 9090],
   [23, 56, 72]]

print(f(T, N))
