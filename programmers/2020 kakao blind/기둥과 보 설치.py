def is_right_bo(builds, x, y):
    if '기' in builds[y - 1][x] or '기' in builds[y - 1][x + 1] or ('보' in builds[y][x - 1] and '보' in builds[y][x + 1]):
        return True
    else:
        return False


def is_right_gi(builds, x, y):
    if y == 0 or '기' in builds[y - 1][x] or '보' in builds[y][x - 1] or '보' in builds[y][x]:
        return True
    else:
        return False


def solution(n, build_frame):
    answer = []
    builds = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

    for build in build_frame:
        x, y, a, b = build
        # 설치
        if b == 1:
            # 기둥
            if a == 0:
                if y == 0 or '기' in builds[y - 1][x] or '보' in builds[y][x - 1] or '보' in builds[y][x]:
                    builds[y][x].append('기')
            # 보
            if a == 1:
                if y > 0:
                    if '기' in builds[y - 1][x] or '기' in builds[y - 1][x + 1] or ('보' in builds[y][x - 1] and '보' in builds[y][x + 1]):
                        builds[y][x].append('보')
        # 삭제
        if b == 0:
            # 기둥
            if a == 0:
                builds[y][x].remove('기')
                if is_right_gi(builds, x, y + 1) and is_right_bo(builds, x, y + 1) and is_right_bo(builds, x - 1,y + 1):
                    pass
                else:
                    builds[y][x].append('기')
            # 보
            if a == 1:
                builds[y][x].remove('보')
                if is_right_gi(builds, x + 1, y) and is_right_gi(builds, x, y) and is_right_bo(builds, x - 1,y) and is_right_bo(builds, x + 1, y):
                    pass
                else:
                    builds[y][x].append('보')

    for i in range(n + 1):
        for j in range(n + 1):
            if '보' in builds[i][j]:
                answer.append([j, i, 1])
            if '기' in builds[i][j]:
                answer.append([j, i, 0])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer


# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
#                    [3, 2, 1, 1]]))
# print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
#                    [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))

print(solution(4, [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1]]))
