import math


def new_boarders(boarders, i):
    global t

    for it in range(0, 3):
        if it % 2:
            if boarders[it] < t[i][it]:
                boarders[it] = t[i][it]
        else:
            if boarders[it] > t[i][it]:
                boarders[it] = t[i][it]

    return boarders


def overlapping(boarders, j):
    global t
    x = [0, 0]

    for it in range(0, 3):
        if t[j][it] >= boarders[0 + 2 * it//2] and t[j][it] <= boarders[1 + 2 * it//2]:
            x[it//2] = 1

    return x[0] or x[1]


def area(i):
    return (t[i][1] - t[i][0]) ** 2


def square(i = 0, boarders = [-math.inf, -math.inf, -math.inf, -math.inf], number_of_squares = 1, c_sum = 0, needed_sum = 13):
    global flag
    global t
    print(number_of_squares, i, c_sum)
    if flag == 0 and c_sum <= needed_sum:
        boarders = new_boarders(boarders, i)

        if number_of_squares == 13 and c_sum == needed_sum:
            flag = 1
            return 1

        for j in range(i, len(t)):
            if overlapping(boarders, j) == 0:
                return square(j, boarders, number_of_squares + 1, c_sum + area(j))

    return 0


def launch():
    for i in range(0, len(t)):
        if flag == 0:
            return square(i, [-math.inf, -math.inf, -math.inf, -math.inf], 1, area(i))


flag = 0
t = [[1, 2, 1, 2],
     [3, 4, 3, 4],
     [5, 6, 5, 6],
     [3, 6, 3, 6], # ten nieużyty
     [7, 8, 7, 8],
     [9, 10, 9, 10],
     [11, 12, 11, 12],
     [13, 14, 13, 14],
     [15, 16, 15, 16],
     [17, 18, 17, 18],
     [20, 21, 20, 21],
     [22, 23, 22, 23],
     [24, 25, 24, 25],
     [26, 27, 26, 27],
     [1, 7, 1, 7]] # ten też nieużyty


print(launch())