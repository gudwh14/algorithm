import collections
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = collections.Counter(nums)
        sort_counts = sorted(counts.items(), key=lambda x: x[0], reverse=True)
        Q = []
        for key, value in sort_counts:
            heapq.heappush(Q, (key, value))
            k -= value
            if k <= 0:
                return heapq.heappop(Q)[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # k 번째 만큼 가장 큰값부터 순서대로 리스트로 리턴된다, nsmallest() 작은값
        return heapq.nlargest(k, nums)[-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]



s = Solution()
print(s.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
print(s.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))