from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = []
        vertices = defaultdict(set)
        vertices.update((k, set()) for k in range(n))
        for [a, b] in edges:
            vertices[a].add(b)
            vertices[b].add(a)
        queue = deque()
        queue.append(source)
        while queue:
            v = queue.popleft()
            if v == destination:
                return True
            if v in visited:
                continue
            visited.append(v)
            for neighbor in vertices[v]:
                if neighbor == destination:
                    return True
                else:
                    queue.append(neighbor)
        return False


if __name__ == "__main__":
    assert Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    assert not Solution().validPath(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
    assert Solution().validPath(n=1, edges=[], source=0, destination=0)
