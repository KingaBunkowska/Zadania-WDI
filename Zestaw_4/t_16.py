def only_prime_digits (a):
    is_prime_digit=[0, 0, 1, 1, 0, 1, 0, 1, 0, 0]

    while a!=0:
        if is_prime_digit[a%10] == 0:
            return 0

        a //= 10

    return 1


def f(T, N):
    all_exist = 1
    for row in range(N):
        exist = 0
        if exist == 0 and all_exist == 1:
            for col in range(N):
                if only_prime_digits(T[row][col]):
                    exist = 1
                    break

            all_exist = exist

    return all_exist


N= 3
T= [[242, 5860, 891705986],
    [2313, 5703, 72315],
    [17, 25, 11]]

print(f(T, N))





