def to_str(n, base):
    # String to represent digits in bases up to 16
    convert_string = "0123456789ABCDEF"
    if n < base:  # Base case: if n is less than the base
        # Return the corresponding character for the digit
        return convert_string[n]
    else:
        # Recursive case: divide n by base and get the string representation of the quotient
        # Then, append the character for the remainder
        return to_str(n // base, base) + convert_string[n % base]


print(to_str(1453, 16))


# Conversion Steps:
# 1453 in base 16:
# 1453 // 16 = 90 (quotient)
# 1453 % 16 = 13 (remainder, which corresponds to 'D')

# Next step:
# 90 // 16 = 5 (quotient)
# 90 % 16 = 10 (remainder, which corresponds to 'A')

# Final step:
# 5 // 16 = 0 (quotient)
# 5 % 16 = 5 (remainder, which corresponds to '5')
