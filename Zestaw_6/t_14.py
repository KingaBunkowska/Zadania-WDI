def hanoi(a, b, c, n):
    # print(a, b, c, n)
    if n>0:
        hanoi(a, c, b, n-1)
        b.append(a.pop())
        hanoi(c, b, a, n-1)


a = [1, 2, 3]
b = []
c = []

hanoi(a, b, c, 3)
