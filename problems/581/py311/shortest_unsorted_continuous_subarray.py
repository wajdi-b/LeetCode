from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sub_i = len(nums)
        sub_j = 0

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    sub_i = min(sub_i, i)
                    sub_j = max(sub_j, j)
        return 0 if sub_j - sub_i < 0 else sub_j - sub_i + 1


if __name__ == "__main__":
    assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
