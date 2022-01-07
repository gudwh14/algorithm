from typing import List


# 나눗셈을 사용하지 않고 O(n)으로 풀이하라!
# 전체 곱셈값을 구해놓고 자기자신을 나눠서 풀이하는 방법은 안된다!
# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        # 기본값
        p = 1

        # 마지막 원소를 제외한 결과를 저장
        for i in range(0, len(nums)):
            result.append(p)
            p = p * nums[i]

        p = 1
        # 왼쪽의 곱셈결과에 오른쪽 값부터 곱하여 저장
        for i in range(len(nums) - 1, 0 - 1, -1):
            result[i] = result[i] * p
            p = p * nums[i]

        return result


s = Solution()
print(s.productExceptSelf(nums=[1, 2, 3, 4]))
print(s.productExceptSelf(nums=[-1, 1, 0, -3, 3]))
print(s.productExceptSelf(nums=[0, 0, -1]))
print(s.productExceptSelf(nums=[0, -1]))
print(s.productExceptSelf(nums=[0, 0]))
