# 접근법
# 거리가 가장먼 곳부터 배달하고 수거해야 무조건 이동하는 거리가 최소임
# 즉, 뒤에서 부터 배달하고 수거하면 댐
# 근데 왜 구현이 안대지... (코드 참조문제)

def solution(cap, n, deliveries, pickups):
    answer = 0
    deli, pick = 0, 0

    for pos in range(n - 1, -1, -1):
        deli += deliveries[pos]
        pick += pickups[pos]

        # print(pos, deli, pick)
        # 이동조건
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (pos + 1) * 2
        # deli, pick이 음수면 음수인 개수만큼 배달, 수거 가능

    return answer