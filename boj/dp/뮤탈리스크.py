def solution(N, scvs):
    INF = float('+inf')
    answer = INF
    dp = [[[INF for _ in range(61)] for _ in range(61)] for _ in range(61)]

    while len(scvs) < 3:
        scvs.append(0)

    def attack(scv1, scv2, scv3, count):
        # scv가 다죽으면 카운트 할당
        if scv1 <= 0 and scv2 <= 0 and scv3 <= 0:
            nonlocal answer
            answer = min(answer, count)
            return

        # scv 체력이 -로 떨어졌을경우 0으로 세팅
        if scv1 < 0:
            scv1 = 0

        if scv2 < 0:
            scv2 = 0

        if scv3 < 0:
            scv3 = 0

        # 만약 현재 해당 scv 체력에 대한 카운트가 dp에있는 카운트보다 더 크면 더이상 탐색할 필요 없음
        # 최소로 공격하는 횟수를 구하기 때문
        if dp[scv1][scv2][scv3] <= count:
            return

        dp[scv1][scv2][scv3] = count

        attack(scv1 - 9, scv2 - 3, scv3 - 1, count + 1)
        attack(scv1 - 9, scv2 - 1, scv3 - 3, count + 1)
        attack(scv1 - 3, scv2 - 9, scv3 - 1, count + 1)
        attack(scv1 - 1, scv2 - 9, scv3 - 3, count + 1)
        attack(scv1 - 1, scv2 - 3, scv3 - 9, count + 1)
        attack(scv1 - 3, scv2 - 1, scv3 - 9, count + 1)

    attack(scvs[0], scvs[1], scvs[2], 0)

    return answer


N = int(input())
scvs = list(map(int, input().split()))
print(solution(N, scvs))
