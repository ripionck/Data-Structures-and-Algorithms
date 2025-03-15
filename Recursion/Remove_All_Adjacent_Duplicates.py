def remove_all_adjacent_duplicates(s):
    # Base case: if the string is empty or has only one character, return as it is
    if len(s) <= 1:
        return s

    # Initialize result string
    result = []

    # Iterate through the string
    i = 0
    while i < len(s):
        # If current character is different from the next one, add it to result
        if i == len(s) - 1 or s[i] != s[i+1]:
            result.append(s[i])
            i += 1
        else:
            # Skip all adjacent duplicates
            while i < len(s) - 1 and s[i] == s[i+1]:
                i += 1
            i += 1

    # Convert result list to string
    result_str = ''.join(result)

    # If the result is different from the input, recursively call the function
    if result_str != s:
        return remove_all_adjacent_duplicates(result_str)
    else:
        return result_str


string = "abbacad"
print(remove_all_adjacent_duplicates(string))
