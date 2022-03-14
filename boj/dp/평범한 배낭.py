def solution(N, K, infos):
    dp = [0 for _ in range(K + 1)]

    for n in range(N):
        weight = infos[n][0]
        value = infos[n][1]

        # 해당 물건의 무게가, 버틸수 있는 무게보다 무거우면 스킵
        if weight > K:
            continue
        # 배열의 오른쪽 -> 왼쪽으로 탐색하며, 배낭이 업데이트 될때는 항상 현재 탐색하고있는 무게보다 커지므로
        # 현재 배열의 인덱스보다 큰 인덱스를 업데이트 해주게 된다.
        for j in range(K, 0, -1):
            if dp[j] > 0:
                if weight + j <= K:
                    dp[weight + j] = max(dp[weight + j], dp[j] + value)

        dp[weight] = max(dp[weight], value)

    return max(dp)


N, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, infos))
