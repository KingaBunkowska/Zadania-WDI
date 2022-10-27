def is_num_in_seq(a, b, num):
    while b <= num:
        a, b = b, a+b
        if b == num:
            return 1
    return 0

def zad2():
    year = 2022
    ciag_fibbonaciego_rosnacy = True
    curr_sum = 1

    while True:
        for a in range(curr_sum):
            b = curr_sum - a
            if a > b and ciag_fibbonaciego_rosnacy:
                continue
            print(a, b, curr_sum)
            if is_num_in_seq(a, b, year):
                return a, b
        curr_sum += 1

print(zad2())
