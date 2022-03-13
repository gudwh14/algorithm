def solution(n):
    dp = [0 for _ in range(1001)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))
