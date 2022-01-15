from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sums 배열 nums[0]를 한개 가진 배열로 초기화
        sums: List[int] = [nums[0]]

        for i in range(1, len(nums)):
            # sums[i - 1] > 0 크면 누적합 계산 , 0 보다 작으면 버린다
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))

        return max(sums)


# 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_num = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            best_num = max(current_sum, best_num)
            print(current_sum, best_num)

        return best_num


s = Solution()
print(s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(s.maxSubArray(nums=[5, 4, -1, 7, 8]))
