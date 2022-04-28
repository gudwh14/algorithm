import math


# 파이어볼 움직이기
def move_fire(balls):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    # 움직인 파이어볼의 정보를 저장할 dict
    result = {}
    for r, c, m, s, d in balls:
        new_r = (r + directions[d][0] * s) % N
        new_c = (c + directions[d][1] * s) % N

        # 새로운 좌표에 대한 정보면 새롭게 생성
        if (new_r, new_c) not in result:
            result[(new_r, new_c)] = [m, s, d, 1, d % 2]
        # 이미 존재하는 정보면 현재 파이어볼 정보 더하기
        else:
            result[(new_r, new_c)][0] += m
            result[(new_r, new_c)][1] += s
            result[(new_r, new_c)][3] += 1
            result[(new_r, new_c)][4] += d % 2

    return result


def split_fire(balls_info):
    # 새로운 파이어볼 배열
    new_balls = []

    for key, value in balls_info.items():
        r, c = key
        m, s, d, count, direct = value
        # 카운트가 1이면 그대로 파이어볼 만들기
        if count == 1:
            new_balls.append([r, c, m, s, d])
        # 2개 이상이면 질량, 속도, 방향 구하여 4개 파이어볼 만들기
        elif count > 1:
            new_m = math.floor(m / 5)
            new_s = math.floor(s / count)

            if new_m > 0:
                if direct == count or direct == 0:
                    d_arr = [0, 2, 4, 6]
                else:
                    d_arr = [1, 3, 5, 7]
                for d in d_arr:
                    new_balls.append([r, c, new_m, new_s, d])

    return new_balls


def solution(balls):
    answer = 0

    for _ in range(K):
        balls_info = move_fire(balls)
        balls = split_fire(balls_info)

    # K번 반복후 남아있는 파이어볼 질량 구하기
    for r, c, m, s, d in balls:
        answer += m
    return answer


N, M, K = map(int, input().split())
balls = [list(map(int, input().split())) for _ in range(M)]
print(solution(balls))
