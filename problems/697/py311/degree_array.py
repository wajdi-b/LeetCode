from collections import Counter
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        candidate_degrees = possible_degrees(freq_map=freq_map)
        ans = []
        for degree in candidate_degrees:
            first = nums.index(degree)
            last = len(nums) - list(reversed(nums)).index(degree)
            ans.append(last - first)
        return min(ans)


def possible_degrees(freq_map: Counter) -> List[str]:
    degrees = freq_map.most_common()
    max_degree = degrees[0][1]
    return [d[0] for d in degrees if d[1] == max_degree]
