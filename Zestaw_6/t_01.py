import math


def is_prime(a):
    if a<2 or a%2==0 or a%3==0:
        return 0

    for i in range(5, int(math.sqrt(a))+1,2):
        if a%i == 0:
            return 0

    return 1


def find_numbers(T, i=0, number=0):

    if i == len(T) and is_prime(number) and number > 9:
        print(number)
        return 0
    elif i == len(T):
        return 0

    find_numbers(T, i+1, number*10+T[i])
    find_numbers(T, i+1, number)


def lenght(number):
    result = 0
    while number != 0:
        number //= 10
        result += 1

    return result


def f(number):
    T = [0 for _ in range(lenght(number))]
    i = lenght(number)-1
    while number != 0:
        T[i] = number % 10
        number //= 10
        i -= 1

    find_numbers(T)


f(2137)


