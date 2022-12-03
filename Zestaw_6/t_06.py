import math

def f(i, sum_index, sum_ele):
    if sum_index == sum_ele and sum_ele != 0:
        return sum_ele

    if i<len(t):
        a = f(i+1, sum_index, sum_ele)
        b = f(i + 1, sum_index + i, sum_ele + t[i])

        if a == None and b == None:
            return math.inf
        elif a == None:
            return b
        elif b == None:
            return a
        else:
            return min(a, b)


t = [1, 7, 3, 5, 11, 2]
print(f(0, 0, 0))