def print_board(board):
    for bo in board:
        print(bo)
    print()


# 초기 상어 위치정보를 구하는 함수
def init_shark(R, C, sharks):
    # R + 1, C + 1 크기만큼 배열 생성
    new_sharks = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    for shark in sharks:
        r, c, s, d, z = shark
        # 해당좌표에 상어 넣기
        new_sharks[r][c].append([s, d, z])
        # 상어 위치 좌표에 추가하기

    return new_sharks


# 상어 낚시하는 함수
def catch_shark(fisher, sharks):
    size = 0
    # 지면과 가까운 순서부터 탐색
    for i in range(1, R + 1):
        # 상어가 존재하면 해당 상어를 잡고 탈출
        if sharks[i][fisher]:
            # 상어 크기 구하기
            size = sharks[i][fisher][0][2]
            # 상어 삭제
            sharks[i][fisher].clear()
            # 한마리 잡으면 종료
            break
    return size


# 상어 이동 함수
def move_shark(R, C, sharks):
    # 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽 방향으로 이동
    directions = [(), (-1, 0), (1, 0), (0, 1), (0, -1)]
    new_sharks = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

    # 상어 찾기
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            # 상어가 존재하면 이동하기
            if sharks[i][j]:
                shark = sharks[i][j][0]
                s, d, z = shark
                # i 축 방향 이동
                ni, nj = i, j
                # 상어가 제자리로 돌아오는 속력은 2 * (칸의 길이 - 1)
                # 제자리로 돌아오는 속력으로 나눈 나머지 값만 이동하면 시간을 줄일수 있다.
                if d == 1 or d == 2:
                    speed = s % (2 * (R - 1))
                    for _ in range(speed):
                        ni += directions[d][0]
                        nj += directions[d][1]
                        if ni == 0:
                            d = 2
                            ni = 2
                        elif ni == R + 1:
                            d = 1
                            ni = R - 1

                elif d == 3 or d == 4:
                    speed = s % (2 * (C - 1))
                    for _ in range(speed):
                        ni += directions[d][0]
                        nj += directions[d][1]
                        if nj == 0:
                            d = 3
                            nj = 2
                        elif nj == C + 1:
                            d = 4
                            nj = C - 1

                # 상어 이동
                new_sharks[ni][nj].append([s, d, z])

    sharks = new_sharks

    # 상어 먹기
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            # 해당 좌표에서 상어가 2마리 이상이면
            if len(sharks[r][c]) > 1:
                # 사이즈를 기준으로 오름차순 정렬
                sharks[r][c].sort(key=lambda x: x[2])
                # 가장 큰 상어는 마지막 인덱스의 상어
                big_shark = sharks[r][c][-1]
                # 해당 좌표 상어 초기화
                sharks[r][c].clear()
                # 해당 좌표에 가장 큰 상어만 삽입
                sharks[r][c].append(big_shark)
    return sharks


def solution(R, C, sharks):
    answer = 0
    sharks = init_shark(R, C, sharks)
    for fisher in range(1, C + 1):
        answer += catch_shark(fisher, sharks)
        sharks = move_shark(R, C, sharks)
    return answer


R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]

print(solution(R, C, sharks))
