def find_center(t, r, i=0, sum_ele=[0, 0, 0], used=0):
    if i >= len(t) and used >= 3:
        x = sum_ele[0]/used
        y = sum_ele[1]/used
        z = sum_ele[2]/used
        return abs(x) <= r and abs(y)<=r and abs(z)<=r
    elif i>= len(t):
        return 0

    return find_center(t, r, i+1, sum_ele, used) or find_center(t, r, i + 1, [sum_ele[0] + t[i][0], sum_ele[1] + t[i][1], sum_ele[2] + t[i][2]], used +1)



t = [(1, 1, 1), (2, 1, 0), (0, 8, 1)]
r = 1
print(find_center(t, r))