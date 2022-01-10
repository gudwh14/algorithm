from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(elements, index):
            result.append(elements[:])

            for i in range(index, len(nums)):
                dfs(elements + [nums[i]], i + 1)

        dfs([], 0)
        return result


    
