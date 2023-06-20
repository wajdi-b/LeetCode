def add_binary(a: str, b: str) -> str:
    return "".join(format(int(a, 2) + int(b, 2), "b"))


def test_example_1():
    assert add_binary("11", "1") == "100"


def test_example_2():
    assert add_binary("1010", "1011") == "10101"


if __name__ == "__main__":
    test_example_1()
    test_example_2()
