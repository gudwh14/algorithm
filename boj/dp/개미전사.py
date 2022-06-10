def solution(N, K):
    dp = [0] * N
    dp[0] = K[0]
    dp[1] = max(K[0], K[1])

    # Bottom - Up 방식
    for i in range(2, N):
        dp[i] = max(dp[i - 1], dp[i - 2] + K[i])

    # 얻을 수 있는 식량의 최대값 출력
    # Bottom-Up 이기 때문에 마지막 원소값이 최대값이 된다.
    return dp[N - 1]


N = int(input())
K = list(map(int, input().split()))
print(solution(N, K))
