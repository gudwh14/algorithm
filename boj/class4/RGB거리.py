def solution(N, infos):
    dp = [[0, 0, 0] for _ in range(N)]

    def dfs(house):
        dp[house] = infos[house]

        if house + 1 < N:
            dfs(house + 1)

        if house == 0:
            dp[house][0] += min(dp[house + 1][1], dp[house + 1][2])
            dp[house][1] += min(dp[house + 1][2], dp[house + 1][0])
            dp[house][2] += min(dp[house + 1][1], dp[house + 1][0])
        elif house == N - 1:
            pass
        else:
            dp[house][0] += min(dp[house + 1][1], dp[house + 1][2])
            dp[house][1] += min(dp[house + 1][2], dp[house + 1][0])
            dp[house][2] += min(dp[house + 1][1], dp[house + 1][0])

    dfs(0)
    return min(dp[0])


N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, infos))
