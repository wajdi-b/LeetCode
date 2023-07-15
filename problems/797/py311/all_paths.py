from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        destination = len(graph) - 1
        possible_paths = []
        queue = deque([[source]])
        while queue:
            path = queue.popleft()
            if path[-1] == destination:
                possible_paths.append(path)
            for neighbor in graph[path[-1]]:
                queue.append(path + [neighbor])
        return possible_paths


if __name__ == "__main__":
    Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []])
