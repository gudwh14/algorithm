import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


# 보드 초기화 함수
def init_board(N, M, board, passenger):
    # 기존 벽을 -1 로 변경
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board[i][j] = -1
    # 승객 위치를 승객번호대로 board에 표현
    for idx in range(M):
        i = passenger[idx][0] - 1
        j = passenger[idx][1] - 1
        board[i][j] = idx + 1


# 최단 거리 승객 찾는 함수
def find_short_passenger(N, board, start):
    # 택시가 이동할 방향
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    # 방문 배열
    visit = [[False for _ in range(N)] for _ in range(N)]
    Q = collections.deque()
    # 초기 값을 시작 좌표와, 0거리로 설정
    Q.append((start[0], start[1], 0))
    # 방문 처리
    visit[start[0]][start[1]] = True
    min_distance = (float('+inf'), float('+inf'), float('+inf'))

    while Q:
        i, j, distance = Q.popleft()
        # 해당 좌표에 승객이 있으면, 최단거리 판단
        if board[i][j] > 0:
            di, dj, now_distance = min_distance
            if distance < now_distance:
                min_distance = (i, j, distance)
            # 거리가 같으면 행, 열이 작은순
            elif distance == now_distance:
                if i < di:
                    min_distance = (i, j, distance)
                elif i == di:
                    if j < dj:
                        min_distance = (i, j, distance)

        for direct in directions:
            new_i = i + direct[0]
            new_j = j + direct[1]

            if 0 <= new_i < N and 0 <= new_j < N and board[new_i][new_j] > -1 and not visit[new_i][new_j]:
                Q.append((new_i, new_j, distance + 1))
                visit[new_i][new_j] = True

    pi, pj, pdistance = min_distance
    # 승객을 못태울때
    if pdistance == float('+inf'):
        return -1, -1, float('+inf')
    # 시작 지점을 해당 승객을 태운 좌표로 변경
    start = [pi, pj]
    # 몇번 승객인지 저장
    idx = board[pi][pj]
    # board에서 승객 제거
    board[pi][pj] = 0

    return start, idx, pdistance


def move_to_dest(N, board, idx, start, passenger):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    Q = collections.deque()
    Q.append((start[0], start[1], 0))
    visit[start[0]][start[1]] = True
    # 목적지 까지 거리
    min_distance = float('+inf')

    while Q:
        i, j, distance = Q.popleft()
        # 택시 좌표가 목적지이면 거리 설정
        if (i, j) == (passenger[idx - 1][2] - 1, passenger[idx - 1][3] - 1):
            min_distance = min(min_distance, distance)

        for direct in directions:
            new_i = i + direct[0]
            new_j = j + direct[1]

            if 0 <= new_i < N and 0 <= new_j < N and board[new_i][new_j] > -1 and not visit[new_i][new_j]:
                Q.append((new_i, new_j, distance + 1))
                visit[new_i][new_j] = True

    return [passenger[idx - 1][2] - 1, passenger[idx - 1][3] - 1], min_distance


def solution(N, M, fuel, board, start, passenger):
    # 승객을 태운 횟수
    count = 0
    # board 초기화 하기
    init_board(N, M, board, passenger)
    # 시작 좌표 설정
    start = [start[0] - 1, start[1] - 1]

    while True:
        # 승객을 다 태우면 종료!
        if count == M:
            break
        # 최단 거리 승객 찾기
        start, idx, distance = find_short_passenger(N, board, start)
        # 승객을 태울 수 없으면 실패
        if distance == float('+inf'):
            return -1
        # 거리 만큼 연료 감소
        fuel -= distance
        # 더이상 이동할 연료가 없으면 실패
        if fuel < 0:
            return -1
        # 해당 목적지로 이동
        start, distance = move_to_dest(N, board, idx, start, passenger)
        # 거리 만큼 연료 감소
        fuel -= distance
        # 연료가 0 밑으로 떨어지면 실패!
        if fuel < 0:
            return -1
        # 연료를 이동한 거리의 * 2 만큼 충전
        fuel += (distance * 2)
        # 승객 카운팅 + 1
        count += 1

    return fuel


N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
start = list(map(int, input().split()))
passenger = [list(map(int, input().split())) for _ in range(M)]

print(solution(N, M, fuel, board, start, passenger))
