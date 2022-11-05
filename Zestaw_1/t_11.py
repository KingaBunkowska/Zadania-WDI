def sum_of_aliquot(a):
    sum = 1
    for i in range(a-1, 1, -1):
        if a % i == 0:
            sum += i

    return sum

for n in range(1, 1000001):
    x = sum_of_aliquot(n)
    if n == sum_of_aliquot(x) and x > n:
        print(n, x)
