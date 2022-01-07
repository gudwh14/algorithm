from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1, rev2 = [], []

        # l1 연결리스트 값을 배열로 변환 insert를 이용하여 역순으로 저장
        while l1:
            rev1.insert(0, l1.val)
            l1 = l1.next

        # l2 연결리스트 값을 배열로 변환 insert를 이용하여 역순으로 저장
        while l2:
            rev2.insert(0, l2.val)
            l2 = l2.next

        # 배열에 저장된 값을 숫자형식으러 변환
        num1 = int(''.join(str(e) for e in rev1))
        num2 = int(''.join(str(e) for e in rev2))

        # 저장된 숫자를 역순된 연결리스트로 만들기
        str_result = str(num1 + num2)
        head: ListNode = None
        for num in str_result:
            node = ListNode(num)
            node.next = head
            head = node

        return head