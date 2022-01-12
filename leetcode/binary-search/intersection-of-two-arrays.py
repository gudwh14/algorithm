from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        if len(nums1) >= len(nums2):
            for num in nums2:
                if num in nums1:
                    result.append(num)
        else:
            for num in nums1:
                if num in nums2:
                    result.append(num)

        return result


s = Solution()
print(s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))