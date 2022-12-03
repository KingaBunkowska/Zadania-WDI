def balance(i, left, right):

    if left == right:
        return 1

    if i == len(t):
        return 0

    return balance(i+1, left + t[i], right) or balance(i+1, left, right)


t = [1, 2, 5, 10]
a = 17

print(balance(0, 0, a))