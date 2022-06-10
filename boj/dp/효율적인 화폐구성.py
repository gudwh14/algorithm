def solution(N, M, coins):
    # N: 화폐 개수, M: 만들고 싶은 금액
    dp = [float('+inf')] * (M + 1)
    dp[0] = 0

    # 각 화폐마다 반복
    for i in range(N):
        # coins[i]원 부터 M원까지 dp 테이블 초기화
        for j in range(coins[i], M + 1):
            # 만약 j금액에서 현재 코인으로 뺄수 있으면 만들 수 있는 금액이면
            # min(원래 현재금액을 만드는 횟수, 새롭게 현재 금액을 만드는 횟수)
            if dp[j - coins[i]] != float('+inf'):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    return -1 if dp[M] == float('+inf') else dp[M]


N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
print(solution(N, M, coins))
