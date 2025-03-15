# Sum of digits in a string
def sum_of_digits(s):
    # if the string is empty, return 0
    if not s:
        return 0
    # check if the first character is a digit
    first_char = s[0]
    if first_char.isdigit():
        # Convert the character to an integer and add it to the sum of the rest of the string
        return int(first_char) + sum_of_digits(s[1:])
    else:
        # If the first character is not a digit, just continue with  the rest of the string
        return sum_of_digits(s[1:])


string = "a1b2c3d4"
print(sum_of_digits(string))
