def length_of_string(s):
    # if the string is empty, return 0
    if s == "":
        return 0
    # return 1 plus the lenght of the rest of the string
    return 1 + length_of_string(s[1:])


string = "Hello World"
print(length_of_string(string))
