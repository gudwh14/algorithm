import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]


# DP 알고리즘 방식
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num


s = Solution()
print(s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
