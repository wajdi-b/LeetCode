from typing import List


def max_area(height: List[int]) -> int:
    max_area = 0
    i = 0
    j = len(height) - 1

    while j > i:
        i_h = height[i]
        j_h = height[j]

        if i_h > j_h:
            value = j_h * (j - i)
            j -= 1
        else:
            value = i_h * (j - i)
            i += 1
        max_area = value if value > max_area else max_area
    return max_area


def test_example_1():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_2():
    assert max_area([1, 1]) == 1


if __name__ == "__main__":
    test_example_1()
    test_example_2()
