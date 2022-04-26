import collections


# 초기 상어의 위치를 구하고 해당칸 초기화 하기
def calc_location(N, board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                shark = (i, j)
                board[i][j] = 0
                return shark


# 상어가 한칸씩 이동하여 먹을수 있는 최단거리의 물고기들 찾기
def move_shark(board, shark_size, shark):
    i, j = shark
    Q = collections.deque()
    Q.append((i, j, 0))
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    visit = [[False] * N for _ in range(N)]
    visit[i][j] = True
    min_distance = float('+inf')
    fishes = []

    while Q:
        ni, nj, distance = Q.popleft()

        if 0 < board[ni][nj] < shark_size and min_distance == float('+inf'):
            min_distance = distance

        if 0 < board[ni][nj] < shark_size and min_distance == distance:
            fishes.append((ni, nj, distance))
            continue

        if min_distance != float('+inf') and distance > min_distance:
            continue

        for direct in directions:
            next_i = ni + direct[0]
            next_j = nj + direct[1]

            if 0 <= next_i < N and 0 <= next_j < N and not visit[next_i][next_j]:
                if board[next_i][next_j] <= shark_size:
                    Q.append((next_i, next_j, distance + 1))
                    visit[next_i][next_j] = True

    return fishes


def solution(N, board):
    answer = 0
    shark_size = 2
    eat_count = 0
    shark = calc_location(N, board)

    while True:
        # 최단 거리 물고기 찾기
        fishes = move_shark(board, shark_size, shark)
        # 먹을수 있는 물고기가 없으면 종료
        if not fishes:
            break
        # 물고기 정렬
        fishes.sort(key=lambda x: (x[2], x[0], x[1]))
        # 물고기 먹기
        f_r, f_c, distance = fishes[0]
        eat_count += 1
        if eat_count >= shark_size:
            eat_count = 0
            shark_size += 1
        shark = (f_r, f_c)
        answer += distance
        board[f_r][f_c] = 0
    return answer


N = int(input().split()[0])
board = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, board))
