import math


def f(t, i=0, sumx=0, sumy=0, ele=0):
    global res

    if i == len(t) and ele!=0:
        res.append((sumx/ele, sumy/ele))

    if i<len(t):
        f(t, i+1, sumx, ele)
        f(t, i+1, sumx+t[i][0], sumy + t[i][1], ele + 1)


def smallest_distance():
    global res
    Min = math.inf
    for i in range(0, len(res)-1):
        for j in range(i, len(res)):
            distance = abs(math.sqrt((res[j][0]-res[i][0])**2) + ((res[j][1] - res[i][1])**2))
            if Min > distance and i!=j:
                Min = distance

    return Min





t = [(1, 0), (8, 1), (2, 3)]
ires = 0
res = []

f(t)
print(smallest_distance())