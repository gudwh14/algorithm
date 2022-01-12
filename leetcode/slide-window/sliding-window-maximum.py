import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        result = []

        for i, n in enumerate(nums):
            # k 크기의 슬라이딩 윈도우를 위해 큐의 첫번째 index 값과 현재 인덱스값의 차이가 k 이면
            # popleft() 하여 크기를 k개만큼 지켜준다
            if deque and i - deque[0] == k:
                deque.popleft()

            # 마지막 max 값과 비교해 더 큰값이면 pop 하고 새로운 max 값 push
            while deque and n > nums[deque[-1]]:
                deque.pop()

            deque.append(i)

            # k 번째 부터 결과 리스트에 저장
            if i >= k - 1:
                result.append(nums[deque[0]])

        return result


s = Solution()
print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(s.maxSlidingWindow(nums=[1, -1], k=1))
