x = int(input())
a, b = x, 1
e = 10e-8 #epsilon - blad pomiaru

while a - b > e:
    a = (a+b)/2
    b = x/a

print(a)