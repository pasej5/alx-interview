def pascal_triangle(n):
    """Generate Pascal's Triangle up to the nth row.

    Args:
    - n (int): Number of rows to generate in Pascal's Triangle.

    Returns:
    - list of lists: Pascal's Triangle as a list of lists of integers.
      Returns an empty list if n <= 0.
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        current_row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                current_row.append(1)
            else:
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                current_row.append(value)
        triangle.append(current_row)

    return triangle
