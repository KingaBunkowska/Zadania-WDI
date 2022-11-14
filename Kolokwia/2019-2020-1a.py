import math

def suma_ele(t, i, n, N):
    if i+n >= N:
        return -math.inf
    else:
        result = 0
        for x in range(i, n+i):
            result += t[x]

        return result


def f(t1, t2, N):
    for size1 in range(1, 24):
        size2 = 24-size1
        for i1 in range(0,N-size1):
            for i2 in range(0, N-size2):
                a = suma_ele(t1, i1, size1, N)
                b = suma_ele(t2, i2, size2, N)
                x = 2
                while x*x<=(a+b):
                    x += 1

                x -= 1
                if x*x==(a+b):
                    return 1

    return 0


T1= [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
T2 =[0,0,0,0,0,1,1,0,0,0,0,1,1,1]
N = 14

print(f(T1, T2, N))
