from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    width = len(matrix[0])
    height = len(matrix)
    top_boundary = left_boundary = 0
    bottom_boundary = height - 1
    right_boundary = width - 1

    visited = []

    while len(visited) < width * height:
        for i in range(left_boundary, right_boundary + 1):
            visited.append(matrix[top_boundary][i])
        for j in range(top_boundary + 1, bottom_boundary + 1):
            visited.append(matrix[j][right_boundary])
        if bottom_boundary != top_boundary:
            for i in range(right_boundary - 1, left_boundary - 1, -1):
                visited.append(matrix[bottom_boundary][i])
        if left_boundary != right_boundary:
            for j in range(bottom_boundary - 1, top_boundary, -1):
                visited.append(matrix[j][left_boundary])
        top_boundary += 1
        right_boundary -= 1
        bottom_boundary -= 1
        left_boundary += 1
    return visited


def test_example_1():
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_example_2():
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
