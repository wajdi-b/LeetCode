def longest_palindrome(s: str) -> str:
    for length in range(len(s), 0, -1):
        for start in range(len(s) - length + 1):
            if is_palindrome(s[start : start + length]):
                return s[start : start + length]
    return ""


def is_palindrome(s: str) -> bool:
    return s[::-1] == s


def test_example_1():
    assert is_palindrome("bab")
    assert not is_palindrome("baba")


if __name__ == "__main__":
    # test_example_1()
    print(longest_palindrome("aghsdfytewtifguewyfgvbababababab"))
