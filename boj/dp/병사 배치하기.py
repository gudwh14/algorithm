def solution(N, soldiers):
    # 병사 정보를 뒤집어 최장 증가 부분 수열 문제로 치환
    # 기본값은 1
    dp = [1] * N
    soldiers.reverse()

    # LIS를 구하는 로직
    for i in range(1, N):
        for j in range(i):
            if soldiers[j] < soldiers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return N - max(dp)


N = int(input())
soldiers = list(map(int, input().split()))
print(solution(N, soldiers))
