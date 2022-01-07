from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head

        while list1 and list2:
            # 2번 연결리스트의 값이 더크면 node 연결리스트에 1번 연결리스트 할당
            if list1.val < list2.val:
                node.next = list1
                # 1번 연결리스트 이동
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # 비교가 모두 끝난후 연결리스트가 남아있을경우
        if list1:
            node.next = list1
        elif list2:
            node.next = list2

        # node 는 맨마지막 None 을 가르키고 있기때문에 head를 통해 반환
        return head.next
