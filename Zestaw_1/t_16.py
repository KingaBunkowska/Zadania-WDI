def ciag(a):
    i = 0
    x = a
    while x != 1:
        x = (x % 2) * ((3 * x) + 1) + (1 - (x % 2)) * (x / 2)
        i += 1

    return i

Max, MaxA =  0, 0
for a in range(2, 10001):
    steps = ciag(a)
    if steps > Max:
        Max = steps
        MaxA = a

print(MaxA, Max)