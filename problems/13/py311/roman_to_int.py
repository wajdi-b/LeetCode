def roman_to_int(s: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    last = len(s) - 1
    result = roman_map[s[last]]

    for i in range(last - 1, 0, -1):
        if s[i] < s[i + 1]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    return result


def test_example_1() -> int:
    roman_to_int("III")


def test_example_2() -> int:
    roman_to_int("LVIII")


def test_example_3() -> int:
    roman_to_int("MCMXCIV")


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
