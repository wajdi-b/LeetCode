from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    h = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s in h.keys():
            h[sorted_s].append(s)
        else:
            h[sorted_s] = [s]
    return list(h.values())


def test_example_1():
    assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["bat"],
        ["nat", "tan"],
        ["ate", "eat", "tea"],
    ]


def test_example_2():
    assert group_anagrams([""]) == [[""]]


def test_example_3():
    assert group_anagrams(["a"]) == [["a"]]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
