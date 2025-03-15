# Iterative approach
"""def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
"""

# Recursive approach
"""def count_vowels(s):
    vowels = "aeiouAEIOU"
    if len(s) == 0:
        return 0

    if s[0] in vowels:
        count = 1
    else:
        count = 0

    return count + count_vowels(s[1:])
"""


def count_vowels(s):
    vowels = "'aeiouAEIOU"
    if not s:
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])


string = "A Quick Brown Fox Jumped Over the Lazy Dog"
print(count_vowels(string))
