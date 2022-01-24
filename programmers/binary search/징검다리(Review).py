def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = 0

    while left <= right:
        # 이전돌
        prev = 0
        # 돌 거리 최솟값
        _min = float('+inf')
        # 제거 한 돌 개수
        remove = 0

        # 바위 사이 최소 거리
        mid = (left + right) // 2
        # 각 돌을 돌면서 제거할 돌을 찾는다 ( 최소 거리가 안되면 바위 제거 )
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                if i != len(rocks) - 1:
                    remove += 1
            else:
                _min = min(_min, rocks[i] - prev)
                prev = rocks[i]
            if remove > n:
                break
        # 제거한 개수가 기준 보다 많으면 , 제거를 줄여야함
        # 바위 사이 최소거리 기준을 낮춰야 한다
        if remove > n:
            right = mid - 1

        # 제거한 개수가 기존 보다 적으면, 더 많은 바위를 제거해야함
        # 바위 사이 기준을 높여야 한다
        else:
            answer = _min
            left = mid + 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
