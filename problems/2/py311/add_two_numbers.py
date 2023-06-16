from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    node = l1
    n1 = ""
    while node:
        n1 += str(node.val)
        node = node.next
    n1 = "".join(reversed(n1))

    node = l2
    n2 = ""
    while node:
        n2 += str(node.val)
        node = node.next
    n2 = "".join(reversed(n2))
    result = sum(map(int, [n1, n2]))
    node = head = ListNode()
    for a in "".join(reversed(str(result))):
        node.next = ListNode(int(a))
        node = node.next
    return head.next


def test_example_1():
    add_two_numbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))


def test_example_2():
    add_two_numbers(ListNode(), ListNode())


def test_example_3():
    add_two_numbers(
        ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
        ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
    )


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
