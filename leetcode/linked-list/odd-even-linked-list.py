from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head 가 None 일때 처리
        if head is None:
            return None

        # 홀수는 head 를 초기할당
        odd = head
        # 짝수는 head.next 를 초기할당
        even = head.next
        # odd list 뒤에 even list 를 연결하기위해서 even list 를 가르키고 있는 even_head 할당
        even_head = head.next

        # 홀수 , 짝수 노드를 각각 연결리스트에 연결
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        # 홀수리스트를 짝수리스트와 연결
        odd.next = even_head
        return head

