def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


L = [1, 3, 5, 7, 9]
print(list_sum(L))
