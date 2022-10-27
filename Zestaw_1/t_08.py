from math import sqrt

n = int(input())

for i in range(int(sqrt(n)), 2, -1):
    if n % i == 0:
        print(False)
        quit()

print(True)
