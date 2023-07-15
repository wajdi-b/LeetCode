class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = dict.fromkeys(pattern)
        s_arr = s.split()
        if len(s_arr) != len(pattern):
            return False
        for i in range(len(pattern)):
            c = pattern[i]
            if not map[c] and s_arr[i] not in map.values():
                map[c] = s_arr[i]
            else:
                if map[c] != s_arr[i]:
                    return False
        return True
