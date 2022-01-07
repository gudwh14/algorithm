from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return sum(nums[::2])


s = Solution()
print(s.arrayPairSum(nums=[6, 2, 6, 5, 1, 2]))
