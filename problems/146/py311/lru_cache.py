from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.h = OrderedDict()
        assert capacity > 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.h.keys():
            self.h.move_to_end(key, last=False)
            return self.h[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h.keys():
            self.h[key] = value
        else:
            if len(self.h.keys()) >= self.capacity:
                self.h.popitem()
            self.h[key] = value
        self.h.move_to_end(key, last=False)


def test_example_1():
    cache = LRUCache(2)
    cache.put(1, 1)  # cache is {1=1}
    cache.put(2, 2)  # cache is {1=1, 2=2}
    assert cache.get(1) == 1  # return 1
    cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert cache.get(2) == -1  # returns -1 (not found)
    cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert cache.get(1) == -1  # return -1 (not found)
    assert cache.get(3) == 3  # return 3
    assert cache.get(4) == 4  # return 4


def test_example_2():
    cache = LRUCache(2)
    cache.put(1, 0)
    cache.put(2, 2)
    assert cache.get(1) == 0
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_example_3():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
