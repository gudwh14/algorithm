import collections


# Memoization 방식 풀이
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        # fib(0) = 0, fib(1) = 1
        if n <= 1:
            return n

        # 이미 존재하면 계산 하지 않고 결과값 반환
        if self.dp[n]:
            return self.dp[n]

        # 재귀로 피보나치
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


# Bottom - top(상향식 풀이 - 타뷸레이션)
class Solution:
    def fib(self, n: int) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


s = Solution()
print(s.fib(4))
