def split(t, r, k, i=0, sum_x=0, sum_y=0, used=0):
    if k  == used:
        return abs(sum_x/used) <= r and abs(sum_y/used) <= r
    if i >= len(t):
        return 0

    return split(t, r, k, i + 1, sum_x, sum_y, used) or split(t, r, k, i + 1, sum_x + t[i][0], sum_y + t[i][1], used + 1)


t = [(1, 2), (8, 8), (1, 1), (0, 1), (3, 5), (0, 0)]
r = 1
k = 3
print(split(t, r, k))