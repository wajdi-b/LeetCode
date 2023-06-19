from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: Optional[ListNode]) -> bool:
    if head:
        palindrome_postulate = ""
        while head:
            palindrome_postulate += str(head.val)
            head = head.next
        if palindrome_postulate == palindrome_postulate[::-1]:
            return True
    return False
