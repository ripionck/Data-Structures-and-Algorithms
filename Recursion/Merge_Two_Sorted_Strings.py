# Merge two sorted strings lexicographically
def merge_sorted_strings(s1, s2):
    if not s1:
        return s2
    if not s2:
        return s1

    if s1[0] <= s2[0]:
        return s1[0] + merge_sorted_strings(s1[1:], s2)
    else:
        return s2[0] + merge_sorted_strings(s1, s2[1:])


s1 = "ace"
s2 = "bdf"
print(merge_sorted_strings(s1, s2))
