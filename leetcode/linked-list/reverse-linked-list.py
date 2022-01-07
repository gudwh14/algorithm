from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None

        # 연결리스트 역순으로 만들기
        while head:
            # 동시할당을 이용하여 rev에 head 역순으로 연결
            rev, rev.next, head = head, rev, head.next
        return rev

    