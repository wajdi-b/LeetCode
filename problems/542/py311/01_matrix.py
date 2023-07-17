from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distances = mat.copy()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    distances[i][j] = compute_shortest_distance_to_zero(mat, i, j)
                else:
                    distances[i][j] = 0
        print(distances)
        return distances


def compute_shortest_distance_to_zero(mat, i, j) -> int:
    m = len(mat)
    n = len(mat[0])
    queue = deque([(i, j, 0)])
    visited = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        curr = queue.popleft()
        visited.append(curr)
        for dir in directions:
            if 0 <= curr[0] + dir[0] < m and 0 <= curr[1] + dir[1] < n:
                neighbor = (curr[0] + dir[0], curr[1] + dir[1], curr[2] + 1)
                if mat[neighbor[0]][neighbor[1]] == 0:
                    return neighbor[2]
                if neighbor not in visited:
                    queue.append(neighbor)


if __name__ == "__main__":
    assert Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    ]
    assert Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    ]
