
def print_pattern(a):

    num = 1
    for i in range(1, a+1):
        print()
        for j in range(1, i+1):
            print(num, end=" ")  # Print num with a space after
            num += 1


print_pattern(5)


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
