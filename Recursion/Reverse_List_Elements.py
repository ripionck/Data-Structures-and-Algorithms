def elements_rev(L):
    if len(L) == 1:
        return L
    else:
        return elements_rev(L[1:]) + [L[0]]
        # return [L[0]] + elements_rev(L[1:]) # This will not reverse the list


# test = [1, 2, 3, "ab", "abc"]
test = [1, 2, 3, 4, 5]
print(elements_rev(test))
