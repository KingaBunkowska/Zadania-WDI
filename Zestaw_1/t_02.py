if __name__ == "__main__":
    pass

    first_number = 1
    second_number = 1

    for first_number in range(1, 100):
        for second_number in range(1, 100):
            a = first_number+second_number
            b = a+second_number
            while a < 2023:
                a, b = b, a+b
                if a == 2022:
                    print(first_number, second_number)
                    # sys.exit(0)
                    quit(0)
