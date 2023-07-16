from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1_occurence = [i for i, w in enumerate(wordsDict) if w == word1]
        w2_occurence = [i for i, w in enumerate(wordsDict) if w == word2]
        print(w1_occurence)
        print(w2_occurence)
        ans = []
        for o1 in w1_occurence:
            for o2 in w2_occurence:
                ans.append(abs(o2 - o1))
        return min(ans)
