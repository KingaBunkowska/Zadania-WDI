def f(T, goal, curr_product = 1, i = 0, code=""):
    if curr_product == goal and i==len(T): # need to check, because there could be 1, which don't change product, but is a diff solution
        decode_and_list(code)
        return 1
    elif i==len(T):
        return 0

    return f(T, goal, curr_product, i+1, code) + f(T, goal, curr_product * T[i], i+1, code + " " + str(T[i]))


res = []
def decode_and_list(x):
    global res
    x = x[1:]
    res.append(x.split(' '))


T = [0, 10, 0, 0, 0, 2, 5, 1, 0, 0]
goal = 10
code = ""
print(f(T, goal))
print(res)