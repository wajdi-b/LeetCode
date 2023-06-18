from typing import List


def max_area(height: List[int]) -> int:
    n = len(height)
    areas = {}
    for i in range(n - 1):
        index_area = []
        for j in range(i + 1, n):
            index_area.append(min(height[i], height[j]) * (j - i))
        areas[i] = max(enumerate(index_area), key=lambda x: x[1])[1]
    return max(areas.values())


def test_example_1():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2():
    assert max_area([1, 1]) == 1


if __name__ == "__main__":
    test_example_1()
    test_example_2()
