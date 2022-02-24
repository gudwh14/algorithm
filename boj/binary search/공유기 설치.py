import sys

# 이분탐색 기준은 가장 인접한 두 공유기 사이의 거리로 탐색
def solution(N, C, X):
    answer = 0
    # 이분탐색을 위해 정렬
    X.sort()
    # 최소값은 1
    left = 1
    # 최대 거리값은 맨마지막 집 - 맨 처음집 거리
    right = X[-1] - X[0]

    while left <= right:
        mid = (left + right) // 2

        # 가장 처음집에 공유기 설치
        select = X[0]
        # 카운트 는 1부터시작
        count = 1
        # 집들과 거리 비교
        for i in range(1, len(X)):
            # 만약 다음집에 공유기를 박는다고 했을때 탐색하려는 거리보다 크거나 같으면 설치할수있는 집
            if X[i] - select >= mid:
                count += 1
                select = X[i]

        # 설치된 공유기 개수가 C개보다 크거나 같으면
        # 더 넓게 공유기를 설치 할 수 있다는것
        # left 줄이기
        if count >= C:
            left = mid + 1
            answer = max(answer, mid)
        # 설치개수가 C개보다 적으면 right 줄이기
        else:
            right = mid - 1

    return answer


N, C = map(int, input().split())
X = []
[X.append(int(sys.stdin.readline())) for _ in range(N)]

print(solution(N, C, X))
