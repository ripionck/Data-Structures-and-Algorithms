def print_pattern(a):
    for i in range(1, a + 1):
        print()  # Print new line
        for j in range(1, a - i + 1):
            print(" ", end='')  # Print spaces
        for j in range(1, i + 1):
            print(j, end='')  # Print numbers
    print()  # New line at the end


print_pattern(5)


#     1
#    12
#   123
#  1234
# 12345
