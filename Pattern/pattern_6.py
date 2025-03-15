def print_pattern(a):
    for i in range(1, a + 1):
        print()  # Print new line
        # range function is used with three arguments to count down (start, stop, step).
        for j in range(a - i + 1, 0, -1):
            print(j, end='')  # Print numbers in decreasing order
    print()  # New line at the end


print_pattern(5)


# 54321
# 4321
# 321
# 21
# 1
