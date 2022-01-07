import collections
from typing import Optional, List, Deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        link_to_list: Deque = collections.deque()

        if head is None:
            return True

        node = head
        while node is not None:
            link_to_list.append(node.val)
            node = node.next

        while len(link_to_list) > 1:
            if link_to_list.popleft() != link_to_list.pop():
                return False

        return True


# 런너 기법을 사용한 풀이
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        rev = None

        while fast and fast.next:
            # fast 는 두칸씩 이동
            fast = fast.next.next

            # 동시할당 문제
            rev, rev.next, slow = slow, rev, slow.next

        # 입력값이 홀수 일때 처리
        if fast:
            slow = slow.next

        # 팰린드롬 확인 로직
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return not rev


s = Solution()
print(s.isPalindrome(head=[1, 2, 2, 1]))
