def f(x):
    return x**x-2020

e = 10e-6
a = 1
b = 5

while abs(a-b) > e:
    c = (a+b)/2
    if f(c) == 0:
        print(c)
        quit()
    elif f(a) * f(c) > 0:
        print(a)
        a = c
    else:
        print(b)
        b = c

print((a+b)/2)
