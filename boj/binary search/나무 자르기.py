def solution(N, M, trees):
    answer = 0
    trees.sort()

    left = 0
    right = 2000000000
    # 절단기 높이를 기준으로 이분탐색!
    while left <= right:
        mid = (left + right) // 2

        total = 0
        # 해당 절단기로 얻을수 있는 나무 높이 구하기
        for tree in trees:
            if tree > mid:
                total += tree - mid

        # M미터 보다 작으면, 나무를 더 잘라야함 -> 절단기 높이를 낮춰야 한다.
        if total < M:
            right = mid - 1
        # M미터 보다 크거나 같으면, max값을 answer에 저장후, 절단기 높이를 낮춰서 더 큰 값이 있나 탐색하기
        else:
            answer = max(answer, mid)
            left = mid + 1

    return answer


N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(N, M, trees))
