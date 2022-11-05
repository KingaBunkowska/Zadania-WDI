from math import sqrt

def determine_pi():
    prev = 0.5
    result = 1
    x = sqrt(0.5)
    for i in range(1, 10**7):
        prev = result
        result *= x
        x = sqrt(0.5 + (0.5 * x))

    return 2/result

print(determine_pi())

