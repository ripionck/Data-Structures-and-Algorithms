# def reverse_all(L):
#     if len(L) == 1:
#         if type(L[0]) != list:
#             return L
#         else:
#             return [reverse_all(L[0])]

#     else:
#         if type(L[0]) != list:
#             return reverse_all(L[1:]) + [L[0]]
#         else:
#             return reverse_all(L[1:]) + reverse_all(L[0])


# Simplified
def reverse_all_elements(L):
    if L == []:
        return []
    elif type(L[0]) != list:
        return reverse_all_elements(L[1:]) + [L[0]]
    else:
        return reverse_all_elements(L[1:]) + [reverse_all_elements(L[0])]


test = [1, 2, [3, 4], [5, 6, [7, 8, 9]]]
print(reverse_all_elements(test))
