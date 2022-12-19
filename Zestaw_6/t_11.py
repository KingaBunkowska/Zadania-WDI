# Proszę napisać program zliczający liczbę "enek" o określonym iloczynie
# nie rozumiem pytania chyba chodzi o to żeby n liczb mnożyło się dając dany iloczyn, no i trzeba to policzyć

def f(T, goal, curr_product = 1, i = 0):
    if curr_product == goal and i==len(T): # need to check i==len(T), because there could be 1, which don't change product, but is a diff solution
        return 1
    elif i==len(T):
        return 0

    return f(T, goal, curr_product, i+1) + f(T, goal, curr_product * T[i], i+1)


T = [0, 0, 0, 0, 0, 2, 5, 1, 0, 0]
goal = 10
print(f(T, goal))