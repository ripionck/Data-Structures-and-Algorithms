# Iterative approach
"""def generate_pascals_triangle(n):
    triangle = []
    for row_num in range(n+1):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j-1] + triangle[row_num-1][j]
        triangle.append(row)
    return triangle
"""

# Recursive approach


def generate_pascals_triangle(n):
    """
    The function generates Pascal's triangle up to the specified number of rows.

    :param n: The function `generate_pascals_triangle(n)` generates the first n rows of Pascal's
    triangle. Pascal's triangle is a triangular array of binomial coefficients, where each number is the
    sum of the two numbers directly above it in the previous row
    :return: The function `generate_pascals_triangle` returns a list of lists representing Pascal's
    triangle up to the nth row.
    """
    if n == 0:
        return [[1]]
    else:
        triangle = generate_pascals_triangle(n - 1)
        last_row = triangle[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
        return triangle


n = 5
triangle = generate_pascals_triangle(n)
for row in triangle:
    print(row)
