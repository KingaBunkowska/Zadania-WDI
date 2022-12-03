def balance(i, left, right, res = ""):

    if left == right:
        return res[:-1] # chars 0 to len(res) - 1 (to delete unnecessary space)

    if i == len(t):
        return 0

    return balance(i + 1, left + t[i], right, res + str(t[i])+str(' ')) or balance(i + 1, left, right, res) or balance(i + 1, left, right + t[i], res + "-" +str(t[i]) + str(' '))


def reading_res(res):
    return res.split(' ')


t = [1, 2, 5, 10]
a = 4


print(reading_res(balance(0, 0, a))) # it is a list of strings
