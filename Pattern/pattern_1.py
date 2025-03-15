def print_pattern(a):
    """
    Prints a pattern of numbers in increasing order.

    Args:
      a: The number of rows in the pattern.
    """
    for i in range(1, a + 1):
        # Print a newline before each row
        print()
        for j in range(1, i + 1):
            print(i, end="")  # Print i without a newline

# Get the number of rows from the user (optional)
# a = int(input("Enter the value: "))


# Print the pattern for a fixed number of rows (e.g., 5)
print_pattern(5)


# 1
# 22
# 333
# 4444
# 55555
