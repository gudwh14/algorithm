import collections

# 피보나치 유형
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = collections.defaultdict(int)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))