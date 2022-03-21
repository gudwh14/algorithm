import sys


def solution(N, infos):
    dp = [0 for _ in range(N + 1)]

    for day in range(0, N):
        next_day = infos[day][0] + day
        # 일을 완료한 날의 최대 수익은 max(완료한 날의 수익, 오늘까지의 수익 + 일해서 얻는 수익)
        if next_day <= N:
            dp[next_day] = max(dp[next_day], dp[day] + infos[day][1])

        # 각 day별 최대 수익은 max(dp[day-1], dp[day])이다.
        # 상담을 하지않고 날을 건널 뛸 수 있기 때문에
        # 해당 day 상담을 수행하기전 업데이트
        dp[day + 1] = max(dp[day + 1], dp[day])
    return dp[N]


N = int(input())
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution(N, infos))
