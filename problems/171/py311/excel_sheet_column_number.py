def title_to_number(column_title: str) -> int:
    result = 0

    for i in range(len(column_title)):
        result *= 26
        result += ord(column_title[i]) - ord("A") + 1
    return result


def test_example_1():
    assert title_to_number("A") == 1


def test_example_2():
    assert title_to_number("AB") == 28


def test_example_3():
    assert title_to_number("ZY") == 701


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
