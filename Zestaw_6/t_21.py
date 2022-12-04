import random


def find_sum(t, act_sum, col=0, cur_sum=0, first_call = 1):
    if act_sum == cur_sum and first_call != 1:
        return 1

    if col>=len(t):
        return 0

    res = 0
    for row in range(0, len(t)):
        if legal_rows[row] and not res:
            legal_rows[row] = 0
            res = find_sum(t, act_sum, col + 1, cur_sum + t[row][col], 0)
            legal_rows[row] = 1

    if res == 0:
        res = find_sum(t, act_sum, col + 1, cur_sum, first_call)

    return res


t = [[random.randint(0,9) for _ in range(8)] for _ in range(8)]
legal_rows = [1 for _ in range(8)]

print(t)
print(find_sum(t, 7))
