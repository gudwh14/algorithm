# 이분 탐색
def solution(stones, k):
    # left, right 를 나올수있는 최소값, 최대값으로  설정
    left, right = 1, 200000000

    while left <= right:
        mid = (left + right) // 2
        # 건널수 없는 돌 카운팅
        count = 0
        find = False

        # 건널수 없는돌이 k개 만큼 되면 만족
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            if count == k:
                find = True

        # 만족 할수있는 값중 최솟값을 구해야 함으로 찾는값의 범위를 줄여준다
        if find:
            right = mid - 1
        # 만족 하는 값이 아니면 찾는값 범위를 높여주기
        else:
            left = mid + 1

    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([1, 4, 2, 7, 6, 1, 5, 1], 3))
