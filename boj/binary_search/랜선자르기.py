
N, C = map(int, input().split())
house = []

[house.append(int(input())) for _ in range(N)]

def solution():
    answer = 0
    house.sort()

    # binary search
    left = 1
    right = 1000000000

    while left <= right:
        mid = (left + right) // 2

        select = house[0]
        count = 1

        # 그리디?
        # 오름차순으로 정렬되어 있으므로 가장 가까운 인덱스가 최대 거리를 만들 수 있음
        for i in range(1, N):
            if house[i] - select >= mid:
                select = house[i]
                count += 1

        # 설치를 많이 할 수 있으면 거리를 늘릴 수 있음
        if count >= C:
            answer = max(answer, mid)
            left = mid + 1
        # 설치 개수가 부족하면 거리를 좁혀야함
        else:
            right = mid - 1

    print(answer)

solution()
