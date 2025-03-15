def print_pattern(a):
    for i in range(1, a+1):
        print()
        for j in range(1, i+1):
            print(i-j+1, end="")


print_pattern(5)


# 1
# 21
# 321
# 4321
# 54321
