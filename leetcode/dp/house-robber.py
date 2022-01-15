import collections
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        #  입력값이 길이가 2개 보다 작을경우 처리
        if len(nums) <= 2:
            return max(nums)

        # 입력순서 유지를 위해서 OrderedDict 사용
        dp = collections.OrderedDict()
        # 초기값 설정
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 한칸 이상 떨어진 집만 가능한 조건이므로 바로 이전 값이나 ( 한칸 이상 떨어저야 하니 현재값을 더하지 않는다)
            # 한칸 떨어진 값에 현재값을 더한 값중 max 값을 저장한다.
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # dict 에서 마지막 아이템 추출
        return dp.popitem()[1]


s = Solution()
print(s.rob(nums=[2, 7, 9, 3, 1]))
print(s.rob(nums=[1, 2, 3, 1]))
print(s.rob([2, 1, 1, 2]))
