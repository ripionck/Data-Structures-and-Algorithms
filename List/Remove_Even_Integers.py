def remove_even_integers(numbers):
    for num in numbers[:]:  # Iterate over a copy of the list
        if num % 2 == 0:
            numbers.remove(num)
    return numbers


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_integers(my_list)
print(result)
