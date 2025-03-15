def print_pattern(n):
    # First part of the program
    for i in range(1, n+1):
        print()  # Print new line
        for j in range(1, n-i+1):
            print(" ", end='')  # Print spaces
        for j in range(1, i+1):
            print(j, end='')  # Print increasing numbers
        for j in range(1, i):
            print(i-j, end='')  # print decreasing numbers

    # Second part ofthe pattern
    for i in range(1, n+1):
        print()  # Print new line
        for j in range(1, i+1):
            print(" ", end='')  # Print spaces
        for j in range(1, n-i):
            print(j, end='')  # Print increasing numbers
        for j in range(n-i, 0, -1):
            print(j, end='')  # print decreasing numbers
    print()  # New line at the end


if __name__ == "__main__":
    n = int(input("Enter the value: "))
    print_pattern(n)


#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1
