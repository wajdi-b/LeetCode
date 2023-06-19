from typing import List


def array_sign(nums: List[int]) -> int:
    sign = 0
    for n in nums:
        if n == 0:
            return 0
        elif n < 0:
            sign += 1
    return 1 if sign % 2 == 0 else -1


def test_example_1():
    assert array_sign([-1, -2, -3, -4, 3, 2, 1]) == 1


def test_example_2():
    assert array_sign([1, 5, 0, 2, -3]) == 0


def test_example_3():
    assert array_sign([-1, 1, -1, 1, -1]) == -1


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
