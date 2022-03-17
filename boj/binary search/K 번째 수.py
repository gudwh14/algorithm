def solution(N, k):
    left = 1
    right = N * N

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for i in range(1, N + 1):
            count += min(N, mid // i)

        if k <= count:
            right = mid - 1
        elif k > count:
            left = mid + 1

    return left


N = int(input())
k = int(input())
print(solution(N, k))
