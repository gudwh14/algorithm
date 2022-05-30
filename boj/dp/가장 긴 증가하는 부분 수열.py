# DP
# 0 ~ i번째 인덱스에 해당하는 수열의 위치 까지 증가하는 수열의 길이를 저장하여 사용한다.
def solution(N, A):
    dp = [0] * N
    for i in range(N):
        dp[i] = 1
        for j in range(0, i):
            if A[j] < A[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)


N = int(input())
A = list(map(int, input().split()))
print(solution(N, A))
