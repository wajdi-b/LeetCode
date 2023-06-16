from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hash(nums: List[int], target: int) -> List[int]:
    h = {}
    for i in range(len(nums)):
        h[nums[i]] = i
    for i in range(len(nums)):
        if h.get(target - nums[i]) and h.get(target - nums[i]) != i:
            return [i, h.get(target - nums[i])]
    return []


def test_example_1():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_hash([2, 7, 11, 15], 9) == [0, 1]


def test_example_2():
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum_hash([3, 2, 4], 6) == [1, 2]


def test_example_3():
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum_hash([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
