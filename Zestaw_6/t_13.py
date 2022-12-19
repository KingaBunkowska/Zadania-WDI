def division_into_summands(number, t, max_summ=0, i=0): # i checks whether it is first call to forbid one element solution
    if number>0:
        for summ in range(max(1, max_summ), number + i):
            t.append(summ)
            division_into_summands(number - summ, t, summ, 1)
            t.pop()
    elif number == 0:
        print(t)



t = []
division_into_summands(4, t)
