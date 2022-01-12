import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1

        return binary_search(0, len(nums) - 1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
        # 정렬된 순서를 유지하도록 a에 x를 삽입할 위치를 찾습니다.
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


s = Solution()
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
