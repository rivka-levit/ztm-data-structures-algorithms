"""
Given an integer numRows, return the first numRows of Pascal's triangle.

Full description:
https://leetcode.com/problems/pascals-triangle/
"""


def pascal_triangle(num_rows: int) -> list[list[int]]:
    triangle = [list() for _ in range(num_rows)]
    triangle[0].append(1)

    if num_rows > 1:
        triangle[1].extend([1, 1])

        for i in range(2, num_rows):
            triangle[i].append(1)

            for j in range(i-1):
                value = triangle[i-1][j] + triangle[i-1][j+1]
                triangle[i].append(value)
            triangle[i].append(1)

    return triangle
