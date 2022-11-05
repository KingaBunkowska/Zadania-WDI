for n in range(1, 1000001):
    suma = 0
    for i in range(n-1, 0, -1):
        if n % i == 0:
            suma += i

    if suma == n:
        print(n)
