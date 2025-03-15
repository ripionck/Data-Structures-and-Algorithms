def remove_tabs(s):
    if not s:
        return ""
    if s[0] == "\t":
        return remove_tabs(s[1:])
    else:
        return s[0] + remove_tabs(s[1:])


string = "Hello\tWorld"
print(remove_tabs(string))
