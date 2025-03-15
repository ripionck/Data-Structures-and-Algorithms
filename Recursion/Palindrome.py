def is_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()
    # Base case: if the string is empty or has one character
    if len(s) <= 1:
        return True
    # Check the first and last characters
    if s[0] != s[-1]:
        return False
    # Recursive case: check the substring excluding the first and last characters
    return is_palindrome(s[1:-1])


# print(is_palindrome("madam"))
print(is_palindrome("Wassamassaw"))
