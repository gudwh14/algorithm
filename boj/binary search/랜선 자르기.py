def solution(K, N, lans):
    answer = 0
    lans.sort()

    # 이분탐색 기준은 자르는 길이
    left = 1
    right = lans[-1]

    while left <= right:
        mid = (left + right) // 2
        count = 0
        for lan in lans:
            count += lan // mid
        if count < N:
            right = mid - 1
        else:
            answer = max(answer, mid)
            left = mid + 1
    return answer


K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

print(solution(K, N, lans))
